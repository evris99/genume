import platform

def write_to_file(file_path):

    #all of the enumeration info will be stored in this list
    system_details = []

    find_os(system_details)

    fp = open(file_path, "w")
    fp.write("GENUME OUTPUT:\n")

    #writes the info in the text file
    for line in system_details:
        fp.write(line+"\n")

    fp.close()

def find_os(sys_det):
    #finds os version
    sys_det.append("OS: "+ platform.platform())
