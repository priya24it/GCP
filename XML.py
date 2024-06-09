import xml.etree.ElementTree as ET
import sys
from collections import OrderedDict

# modifying the XML file to the required format.
class XMLData:

    def modify_xmldata(self, filename, project_key):
        test_data = OrderedDict()
        try:
            tree = ET.parse(f'./Reports/{filename}')
            root = tree.getroot()
            for tc in root.findall("./testsuite/testcase"):
                if str(tc.attrib['name']).__contains__("["):
                    testcase = str(tc.attrib['name']).replace('[', '').replace(']', '').split('-')
                    testcase_name = str(testcase[1]).split('_')
                    if project_key == "U20":
                        tc.attrib['name'] = "U20-" + str(testcase_name[0])
                    else:
                        tc.attrib['name'] = "QAS-" + str(testcase_name[0])
                    test_key = testcase[1]
                    test_data[test_key] = [tc.attrib['name']]
                    failure_node = tc.find('failure')
                    if failure_node == None:
                        message = "Testcase has passed without any errors."
                        test_data[test_key].append('Pass')
                        test_data[test_key].append(message)
                        log_message = ''
                        test_data[test_key].append(log_message)
                        test_data[test_key].append(tc.attrib['time'])
                    else:
                        message = failure_node.attrib["message"]
                        test_data[test_key].append('Fail')
                        test_data[test_key].append(message)
                        log_message = failure_node.text
                        test_data[test_key].append(log_message)
                        test_data[test_key].append(tc.attrib['time'])
                tree.write(f'./Reports/{filename}')
            return test_data
        except Exception as e:
            print("there is some error while reading the file..", str(sys.exc_info()[0]), str(sys.exc_info()[1]))

