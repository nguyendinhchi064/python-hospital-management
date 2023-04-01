class PatientAndRoom:
  def __init__(self, PatientID, RoomID):
    self.__PatientID = PatientID
    self.__RoomID = RoomID

  def get_PatientID(self):
    return self.__PatientID

  def get_RoomID(self):
    return self.__RoomID

  def set_PatientID(self, id):
    self.__PatientID = id

  def set_RoomID(self, id):
    self.__RoomID = id
    
class PatientAndDoctor:
  def __init__(self, PatientID, DoctorID):
    self.__PatientID = PatientID
    self.__DoctorID = DoctorID

  def get_PatientID(self):
    return self.__PatientID

  def get_DoctorID(self):
    return self.__DoctorID

  def set_PatientID(self, id):
    self.__PatientID = id

  def set_DoctorID(self, id):
    self.__DoctorID = id