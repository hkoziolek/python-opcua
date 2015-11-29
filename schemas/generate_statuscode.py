# Load values from StatusCode.csv and then
# add values from StatusCodes_add.csv, but only
# if they are absent from StatusCode.csv
def status_codes():
    inputfile = open("StatusCodes_add.csv")
    additional = {}
    for line in inputfile:
        name, val, doc = line.split(",", maxsplit=2)
        additional[int(val, 0)] = (name, val, doc)

    inputfile = open("StatusCode.csv")
    result = []
    for line in inputfile:
        name, val, doc = line.split(",", maxsplit=2)
        result.append((name, val, doc))
        additional.pop(int(val, 0), None)
    add = [ additional[k] for k in sorted(additional.keys()) ]
    return add + result

if __name__ == "__main__":
    codes = status_codes()
    outputfile = open("../opcua/status_code.py", "w")
    outputfile.write("#AUTOGENERATED!!!\n")
    outputfile.write("\n")
    #outputfile.write("from enum import Enum\n")
    outputfile.write("\n")

    outputfile.write("class StatusCodes:\n")
    for name, val, doc in codes:
        doc = doc.strip()
        outputfile.write("    {} = {}\n".format(name, val))
    outputfile.write("\n")
    outputfile.write("\n")

    outputfile.write("def get_name_and_doc(val):\n")
    kword = "if"
    for name, val, doc in codes:
        doc = doc.strip()
        doc = doc.replace("'", '"')
        outputfile.write("    {} val == {}:\n".format(kword, val))
        outputfile.write("        return '{}', '{}'\n".format(name, doc))
        kword = "elif"
    outputfile.write("    else:\n".format(val))
    outputfile.write("        return 'UnknownUaError', 'Unknown StatusCode value: {}'.format(val)\n")
    '''
    outputfile.write("class StatusCode(Enum):\n")
    outputfile.write("    Good = 0\n")
    for line in inputfile:
        name, val, doc = line.split(",", maxsplit=2)
        doc = doc.strip()
        outputfile.write("    {} = {}\n".format(name, val))

    outputfile.write("""
    def __new__(self, value=0):
        Enum.__new__(self, value)

    def to_binary(self):
        return struct.pack("!I", self.value)

    @staticmethod 
    def from_binary(data):
        val = struct.unpack("!I", data.read(4))[0]
        sc = StatusCode(val)
        return sc

    def check(self):
        if self.value.name != "Good":
            raise Exception(self.name)
    """)


    #outputfile.write("\n")
    #outputfile.write("\n")
    #outputfile.write("def CheckStatusCode(statuscode):\n")
    #outputfile.write("    if statuscode.data == {}\n")

'''
