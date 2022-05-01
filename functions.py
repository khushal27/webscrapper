from urllib.request import urlopen as uReq
import json
from bs4 import BeautifulSoup as bs
import log

lg = log.logFile()
class ufunc:
    def getBaseURL(self):
        ineuron = "https://courses.ineuron.ai/"
        lg.logging.info("Getting the base URL :"+ineuron)
        return ineuron

    def getBaseDict(self,url):
        # getting the base dictionary of ineuron
        uClientResponse = uReq(url)
        ineuron = uClientResponse.read()
        uClientResponse.close()
        ineuron_html = bs(ineuron, "html.parser")
        ineuronCourse = ineuron_html.find("script", {"id": "__NEXT_DATA__"})
        ineuron_json = json.loads(ineuronCourse.text)
        ineuron_dict = ineuron_json['props']['pageProps']['initialState']['init']
        lg.logging.info("Capturing the base dictionary from base URL")
        return ineuron_dict

    def getCat(self):
        # Courses
        courseDict_list = []
        ineuronbaseURL = self.getBaseURL()
        ineuronDict = self.getBaseDict(ineuronbaseURL)
        for i in ineuronDict['categories'].values():
            courseDict = {}
            courseSubCategory = []
            for j in i['subCategories'].values():
                courseSubCategory.append(j['title'])
            courseDict[i['title']] = courseSubCategory
            courseDict_list.append(courseDict)
        return courseDict_list

    def getCourseDetails(self):
        # course description
        subCourseDesc_list=[]
        ineuronbaseURL = self.getBaseURL()
        ineuronDict = self.getBaseDict(ineuronbaseURL)
        for i in ineuronDict['courses'].keys():
            subCourseDesc = {}
            for j in ineuronDict['courses'].values():
                subCourseDesc[i] = j['description']
            subCourseDesc_list.append(subCourseDesc)
        return subCourseDesc_list

    def getCoursePrice(self):
        # course price
        subCoursePrice_list = []
        ineuronbaseURL = self.getBaseURL()
        ineuronDict = self.getBaseDict(ineuronbaseURL)
        for i in ineuronDict['courses'].items():
            subCoursePrice = {}
            try:
                subCoursePrice[i[0]] = i[1]['pricing']
            except:
                subCoursePrice[i[0]] = ''
            subCoursePrice_list.append(subCoursePrice)
        return subCoursePrice_list

    def getCoursePrice_2(self):
        # course price
        subCoursePrice = {}
        ineuronbaseURL = self.getBaseURL()
        ineuronDict = self.getBaseDict(ineuronbaseURL)
        for i in ineuronDict['courses'].items():
            try:
                subCoursePrice[i[0]] = i[1]['pricing']
            except:
                subCoursePrice[i[0]] = ''
        return subCoursePrice

    def getInstructorDetails(self):
        # instructor
        teacher_list = []
        ineuronbaseURL = self.getBaseURL()
        ineuronDict = self.getBaseDict(ineuronbaseURL)
        for i in ineuronDict['instructors'].keys():
            teacher = {}
            name = ineuronDict['instructors'][i]['name']
            try:
                email = ineuronDict['instructors'][i]['email']
            except:
                email = 'NA'
            try:
                bio = ineuronDict['instructors'][i]['description']
            except:
                bio = 'NA'
            teacher['Name'] = name
            teacher['Email'] = email
            teacher['Bio'] = bio
            teacher_list.append(teacher)
        return teacher_list

    def getCourseURL(self):
        courseURL_List = []
        for i in self.getCoursePrice_2().keys():
            courseURL = {}
            name = i
            url = self.getBaseURL() + i.replace(' ', '-')
            courseURL['CourseName'] = name
            courseURL['URL'] = url
            courseURL_List.append(courseURL)
        return courseURL_List

    def getCourseDict(self,url):
        uClientResponse = uReq(url)
        ineuron = uClientResponse.read()
        uClientResponse.close()
        ineuron_html = bs(ineuron, "html.parser")
        ineuronCourse = ineuron_html.find("script", {"id": "__NEXT_DATA__"})
        ineuron_json = json.loads(ineuronCourse.text)
        try:
            ineuron_dict = ineuron_json['props']['pageProps']['data']['meta']
        except:
            for i in ineuron_json['props']['pageProps']['data']['batches'].values():
                ineuron_dict = i['meta']
        lg.logging.info("Capturing the base dictionary from course URL")
        return ineuron_dict

    def getMainTopics(self, course,url):
        mainTopics = self.getCourseDict(url)
        mainTopics_list=[]
        for i in mainTopics['curriculum'].values():
            mainTopics_dict = {}
            mainTopics_dict['CourseName'] = course
            mainTopics_dict['TopicName'] = i['title']
            mainTopics_list.append(mainTopics_dict)
        return mainTopics_list

    def getOverview(self, url):
        overView = self.getCourseDict(url)
        return overView['overview']