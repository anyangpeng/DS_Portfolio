#safaridriver --enable
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
import json
import time


class Jobsearch():
    __slots = '_account', '_password', '_keywords', '_location', '_title_list', '_location_list'

    def __init__(self, config):
        '''Initializing configuration parameters'''

        self._account = config['account']
        self._password = config['password']
        self._keywords = config['keywords']
        self._location = config['location']
        self._driver = webdriver.Safari()
        self._title_list = []
        self._location_list = []

    def login_linkedin(self):
        """This function logs into your personal LinkedIn profile"""

        print("\n Logging into Linkedin...")
        # go to the LinkedIn login url
        self._driver.get("https://www.linkedin.com/login")

        # introduce email and password and hit enter
        login_email = self._driver.find_element_by_name('session_key')
        login_email.clear()
        login_email.send_keys(self._account)
        login_pass = self._driver.find_element_by_name('session_password')
        login_pass.clear()
        login_pass.send_keys(self._password)
        login_pass.send_keys(Keys.RETURN)
        print("\n Login successfully！")

    def job_search(self):
        """This function goes to the 'Jobs' section a looks for all the jobs that matches the keywords and location"""

        # go to Jobs
        jobs_link = self._driver.find_element_by_link_text('Jobs')
        jobs_link.click()
        time.sleep(2)

        # search based on keywords and location and hit enter
        print("\n Looking for {} jobs in {}".format(
            self._keywords, self._location))
        search_keywords = self._driver.find_element_by_xpath(
            "//input[starts-with(@id,'jobs-search-box-keyword')]")
        search_keywords.clear()
        search_keywords.send_keys(self._keywords)
        search_location = self._driver.find_element_by_xpath(
            "//input[starts-with(@id,'jobs-search-box-location')]")
        search_location.clear()
        search_location.send_keys(self._location)
        time.sleep(1)
        search_location.send_keys(Keys.RETURN)

        # saving current url
        self._current_url = self._driver.current_url
        # get the number of jobs found
        num_jobs = self._driver.find_element_by_class_name(
            "display-flex.t-12.t-black--light.t-normal")
        self._num_jobs_int = int(num_jobs.text.strip().split(" ")
                                 [0].replace(",", ""))
        print("\n {} jobs found.".format(self._num_jobs_int))

    def saving_all_jobs(self):
        """ This function save all jobs from all pages"""

        # get the number of pages
        if self._num_jobs_int > 24:
            find_pages = self._driver.find_elements_by_class_name(
                "artdeco-pagination__indicator.artdeco-pagination__indicator--number")
            total_pages = find_pages[len(find_pages)-1].text
            self._num_pages_int = int(total_pages.strip())

            # saving jobs from the first page
            self._saving_jobs_in_page()
            # saving jobs from rest of the pages
            for i in range(1, self._num_pages_int):
                self._driver.get(self._current_url+'&start='+str(i*25))
                time.sleep(5)
                self._saving_jobs_in_page()
        else:
            self._saving_jobs_in_page()

        self._non_remote_list = list(
            filter(lambda x: ((x != "Remote") & ("$"not in x)), self._location_list))

        df = pd.DataFrame({"Title": self._title_list,
                           "Location": self._non_remote_list})
        df.to_csv('ds_canada.csv', sep='\t', header=True)
        print("All jobs saved!")

    def _saving_jobs_in_page(self):
        '''This function saves all results from the current page into a Dataframe'''

        # Try refreshing page if page is not properly loading
        try:
            reload_button = self._driver.find_element_by_class_name(
                "jobs-search-no-results__reload.artdeco-button.artdeco-button--secondary")
            print("loading problem!!!")
            reload_button.click()
        except ElementNotInteractableException:
            print("Refreshing page!")
            self._driver.refresh()
            time.sleep(5)
        except NoSuchElementException:
            pass
            # crolling down and pre-load all jobs.
        for i in range(6):
            time.sleep(2)
            self._scrolling_page()

        # get job info
        titles = self._driver.find_elements_by_class_name(
            "disabled.ember-view.job-card-container__link.job-card-list__title")
        locations = self._driver.find_elements_by_class_name(
            "job-card-container__metadata-item")
        #
        for title in titles:
            self._title_list.append(title.text.strip())
        for location in locations:
            self._location_list.append(location.text.strip())

        print("\n {}-{} jobs saved!".format(len(self._location_list),
                                            len(self._title_list)))

    def _scrolling_page(self):
        '''This function scrolls down the page'''

        # # locate to the left rail
        # element = self._driver.find_element_by_class_name(
        #     "jobs-search__left-rail")

        # get the current scroll position
        last_height = self._driver.execute_script("return window.scrollY")

        # scroll down only the viewport height window.innerHeight each time
        self._driver.execute_script(
            "window.scrollTo(0, window.scrollY + window.innerHeight);")

    def close_session(self):
        """This function closes the actual session"""

        print('End of the session, see you later!')
        self.driver.close()


if __name__ == '__main__':

    with open('config.json') as config_file:
        config = json.load(config_file)

        search = Jobsearch(config)
        search.login_linkedin()
        time.sleep(5)
        search.job_search()
        search.saving_all_jobs()
        time.sleep(5)
        search.close_session()
