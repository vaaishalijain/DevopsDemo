import argparse 

def parse_argument():
       parse = argparse.ArgumentParser(description="ForTest!")
       parse.add_argument("-test_data")
       parse.add_argument("-build_dir")
       print("Parse: ", parse)

parse_argument()       
print("Run Script")
print("Comment")
