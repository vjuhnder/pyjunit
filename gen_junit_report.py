#!/usr/bin/python3

from junit_xml import TestSuite, TestCase

def testBasicToConsole():
    ''' Perform the very basic test with 1 suite and 1 test case, output to console.
        This is the example from the above referenced pypi webpage, but corrected to
        actually work.
    '''

    test_cases = [TestCase('TestCase1', 'DSPHistograms.noisefloorcalc', 123.345, 'I am stdout!', 'I am stderr!')]
    ts = [TestSuite("TestHistogram", test_cases)]
    # pretty printing is on by default but can be disabled using prettyprint=False
    print(TestSuite.to_xml_string([ts], prettyprint=True))
    with open(r'junit.xml', mode='w') as lFile:
        TestSuite.to_file(lFile, [ts], prettyprint=True)
        lFile.close()

def testBasicInfoToConsole():
    ''' Actually, even more basic than the test above, with classname, stdout, and stderror
        removed to demonstrate they are optional.  For system testing we often won't use them.
        Output to console.
    '''

    test_cases = [TestCase('PathCheck: ApplicationControl', '', .0523, '', '')]
    ts = [TestSuite("DirectorITG2", test_cases)]
    # pretty printing is on by default but can be disabled using prettyprint=False
    print(TestSuite.to_xml_string(ts))

def testFailureInfoToConsole():
    ''' 1 suite and test case with failure info added. Output to console.
    '''

    test_cases = TestCase('FileCheck: DesktopNotificationCenter', '', .0451, '', '')
    test_cases.add_failure_info('Invalid File \'DNC.exe\'.')
    ts = [TestSuite("DirectorITG2", [test_cases])]
    # pretty printing is on by default but can be disabled using prettyprint=False
    print(TestSuite.to_xml_string(ts))

def testMultiTestCasesToConsole():
    ''' Demonstrates a single test suite with multiple test cases, one of which
        has failure info. Output to console.
    '''

    test_cases = [TestCase('FileCheck: DesktopNotificationCenter', '', .0451, '', '')]
    test_cases.append(TestCase('FileCheck: PropertyServer', '', .0452, '', ''))
    test_cases[0].add_failure_info('Invalid File \'DNC.exe\'.')
    ts = [TestSuite("DirectorITG2", test_cases)]
    # pretty printing is on by default but can be disabled using prettyprint=False
    print(TestSuite.to_xml_string(ts))

def testMultiTestSuitesToConsole():
    ''' Demonstrates adding multiple test suites. Output to console.
    '''

    test_cases = [TestCase('FileCheck: DesktopNotificationCenter', '', .0451, '', '')]
    ts = [TestSuite("FileChecks", test_cases)]
    ts.append(TestSuite("ProcessChecks", [TestCase('ProcessCheck: ApplicationControl', '', 1.043, '', '')]))
    # pretty printing is on by default but can be disabled using prettyprint=False
    print(TestSuite.to_xml_string(ts))

def testMultiTestCasesToFile():
    ''' Demonstrates a single test suite with multiple test cases, one of which
        has failure info. Output to a file with PrettyPrint disabled (Jenkins-friendly).
    '''

    test_cases = [TestCase('DesktopNotificationCenter', 'Integration.FileCheck', .0451, '', '')]
    test_cases.append(TestCase('PropertyServer', 'Integration.FileCheck', .5678, '', ''))
    test_cases[0].add_failure_info('Invalid File \'DNC.exe\'.')
    ts = [TestSuite("GII_2013_R1", test_cases)]
    # open the file, then call the TestSuite to_File function with prettyprint off.
    # use raw text here to protect slashes from becoming escape characters
    with open(r'C:\Users\Administrator\.jenkins\workspace\IntegrationTests\FileCheck.xml', mode='a') as lFile:
        TestSuite.to_file(lFile, ts, prettyprint=False)
        lFile.close()


if __name__ == '__main__':
    ''' If this module is being run directly, run all of the example test functions.
        Test functions output JUnit XML for various scenarios to either screen (Console)
        or file.

    '''
    testBasicToConsole()
#    testBasicInfoToConsole()
#    testFailureInfoToConsole()
#    testMultiTestCasesToConsole()
#    testMultiTestSuitesToConsole()
#    testMultiTestCasesToFile()

else:
    ''' Function calls for an external run of this script.

    '''
    testMultiTestCasesToFile()
