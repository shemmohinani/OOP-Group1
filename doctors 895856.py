import re
class Doctor:

    def __init__(self, id, name, specialization, workingTime, qualification, roomNumber):
        self.id = id
        self.name = name
        self.specialization = specialization
        self.workingTime = workingTime
        self.qualification = qualification
        self.roomNumber = roomNumber
        
    def formatDrInfo(propertiesValuesList):
        spaces = [5, 23, 16, 16, 16, 12]
        formattedText = ""
        
        for item in propertiesValuesList:
            formattedText += item + (" " * (spaces[propertiesValuesList.index(item)] - len(item)))
        return formattedText
    
    def enterDrInfo(self):
        self.id = input("Enter the Doctor's ID: \n")
        self.name = input("Enter the Doctor's name: \n")
        self.specialization = input("Enter the Doctor's specialty: \n")
        self.workingTime = input("Enter the Doctor's timing (e.g., 7am-10pm): \n")
        self.qualification = input("Enter the Doctor's qualification: \n")
        self.roomNumber = input("Enter the Doctor's room number: \n")
        
        self.addDrToFile(self)
    
    def readDoctorsFile():
        path = "doctors.txt"
        doctorsObjectList = []
        try:
            file = open(path, 'r')
            lines = file.readlines()
            for line in lines:
                if line.replace(" ", "") != "\n":
                    line = line.replace('\n', '')
                    line = re.split(r'\s{2,}', line)
                    doctor = Doctor(line[0], line[1], line[2], line[3], line[4], line[5])
                    
                    doctorsObjectList.append(doctor)
          
            file.close()
        except IOError:
            file = open(path, 'a+')
            print("doctors.txt file created")
           
        return doctorsObjectList

    def searchDoctorById(idSearch):
        doctorsObjectList = Doctor.readDoctorsFile()
        idExist = False
        for doctor in doctorsObjectList:
            if doctor.id == idSearch:
                doctor.displayDoctorInfo()
                idExist = True
                return doctorsObjectList.index(doctor)
        if idExist == False:
            print("Can't find the doctor with the same ID on the system \n")
            return -1
        
                
    def searchDoctorByName(nameSearch):
        doctorsObjectList = Doctor.readDoctorsFile()
        nameExist = False
        
        for doctor in doctorsObjectList:
            if doctor.name == nameSearch:
                doctor.displayDoctorInfo()
                nameExist = True
        if nameExist == False:
            print("Can't find the doctor with the same name on the system \n")
            return -1
        
    
    def displayDoctorInfo(self):
        headerList = ["ID", "Name", "Specialty", "Timing", "Qualification", "Room Number"]
        print(Doctor.formatDrInfo(headerList) + "\n")
        valuesList = [self.id, self.name, self.specialization, self.workingTime, self.qualification, self.roomNumber]
        print(Doctor.formatDrInfo(valuesList))
        
        
    def editDoctorInfo():
        dr_Id = input("Please enter the id of the doctor that you want to edit their information:\n")
        dr_index = Doctor.searchDoctorById(dr_Id)
        if dr_index != -1:
            drObjList = Doctor.readDoctorsFile()
            drObjList[dr_index].name = input("Enter new Name: \n")
            drObjList[dr_index].specialization = input("Enter new Specialist in: \n")
            drObjList[dr_index].workingTime = input("Enter new Timing: \n")
            drObjList[dr_index].qualification = input("Enter new Qualification: \n")
            drObjList[dr_index].roomNumber = input("Enter new Room Number: \n")
            Doctor.writeListOfDoctorsToFile(drObjList)
        else:
            return -1
        
    def displayDoctorsList():
        path = "doctors.txt"
        headerList = ["ID", "Name", "Specialty", "Timing", "Qualification", "Room Number"]
        headerSpaces = [5, 23, 16, 16, 16, 12]
        for item in headerList:
            print(item + (" " * (headerSpaces[headerList.index(item)] - len(item))), end="")
        print("\n")
        with open(path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                print(line)
        file.close()
        
    def writeListOfDoctorsToFile(doctorsObjectList):
        path = "doctors.txt"
        file = open(path, "r+")
        textOutput = ""
        for dr in doctorsObjectList:
            drProperties = [dr.id, dr.name, dr.specialization, dr.workingTime, dr.qualification, dr.roomNumber]
            ft = Doctor.formatDrInfo(drProperties)
            textOutput += ft + "\n\n"
            
        file.truncate(0)
        file.write(textOutput)
        file.close()
    
    def addDrToFile(drObject):
        path = "doctors.txt"
        textOutput = ""
        
        file = open(path, "a")
        dr = drObject
        drProperties = [dr.id, dr.name, dr.specialization, dr.workingTime, dr.qualification, dr.roomNumber]
        
        addText = Doctor.formatDrInfo(drProperties)
        textOutput += addText + "\n\n"
        file.write(textOutput)
        file.close()
        