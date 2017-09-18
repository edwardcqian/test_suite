#!/usr/bin/env python



# compare files
import filecmp
# filecmp.cmp('file_1', 'file_2')
def cmp_subfile(suite, script):
    test_cnt = 0
    pass_cnt = 0
    with open(suite, 'r') as fstream:
        for test in fstream:
            test_cnt += 1
            # Expected different from actual
            if filecmp.cmp(test+".in", test+".temp") == False: 
                print ("Test failed: %s" %(test)) # print test name
                print ("Expected:")
                with open(test+".out", 'r') as expected:
                    print expected.read()
                print ("Actual:")
                with open(test+".temp", 'r') as actual:
                    print actual.read()
            else:
                pass_cnt += 1
                print ("Test Passed: %s" % test)
            os.remove(test+".temp")
    print ("Test passed %d/%d" % (pass_cnt, test_cnt))
            
            

# run script 
def run_script(suite, script):
    with open(suite, 'r') as fstream:
        for test in fstream:
            os.system("cat %s | python %s >> %s" % (test+".in", script, test+".temp"))


# check for .in and .out
import os.path
def check_subfile(suite):
    with open(suite, 'r') as fstream:
        for test in fstream:
            if os.path.isfile(test+".in") and os.path.isfile(test+".out"):
                return True
            else:
                print(".in or .out for test %s not found" % test)
                return False
                break
        
    

# main
import sys
# open file

if len(sys.argv) != 3: #check for args
    print("The correct usage is: ./runSuite [suite] [script]")
elif check_subfile(sys.argv[1]) == False: #check for .in and .out
    pass
else:
    run_script(sys.argv[1], sys.argv[2])
    cmp_subfile(sys.argv[1], sys.argv[2])
