##define person and address class 
class person:
    def __init__(self,fname,lname,byear,pnumber):
        self.__fname=fname
        self.__lname=lname
        self.__byear=byear
        self.__pnumber=pnumber
    @property
    def fname(self):
        return self.__fname
    @fname.setter
    def fname(self,fname):
        self.__fname=fname 
    @property
    def lname(self):
        return self.__lname
    @lname.setter
    def lname(self,lname):
        self.__lname=lname
    @property
    def byear(self):
        return self.__byear
    @byear.setter
    def byear(self,byear):
        if isinstance(byear,int) and byear>8:
            self.__byear=byear
        else:
            print('please enter valid numbers!')
    @property
    def pnumber(self):
        return self.__pnumber
    @pnumber.setter
    def pnumber(self,pnumber):
        if isinstance(pnumber,int):
            self.__pnumber=pnumber
        else:
            print('please enter only numbers!')

##    def age(self):
##        import datetime
##        now=datetime.datetime.now()
##        return now.year-self.byear
    def __str__(self):
        str1=f"First name:{self.fname}\n"
        str2=f"last name:{self.lname}\n"
        str3=f"Age:{self.byear}\n"
        str4=f"Phone number:{self.pnumber}"
        return str1 + str2 + str3 + str4
##    using __repr__ function to represent objects
    def __repr__(self):
        str1=f"First name:{self.fname}\n"
        str2=f"last name:{self.lname}\n"
        str3=f"Age:{self.byear}\n"
        str4=f"Phone number:{self.pnumber}"
        return str1 + str2 + str3 + str4


class address:
    def __init__(self,city,street,allay,zipcode):
        self.__city=city
        self.__street=street
        self.__allay=allay
        self.__zipcode=zipcode
    @property
    def city(self):
        return self.__city
    @city.setter
    def city(self,city):
        self.__city=city 
    @property
    def street(self):
        return self.__street
    @street.setter
    def street(self,street):
        self.__street=street
    @property
    def allay(self):
        return self.__allay
    @allay.setter
    def allay(self,allay):
        self.__allay=allay
    @property
    def zipcode(self):
        return self.__zipcode
    @zipcode.setter
    def zipcode(self,zipcode):
        if isinstance(zipcode,int):
            self.__zipcode=zipcode
        else:
            print('please enter only numbers!')
    def __str__(self):
        return f"Contact's address:{self.city},{self.street},{self.allay},{self.zipcode}"
##    using __repr__ function to represent objects
    def __repr__(self):
        return f"Contact's address:{self.city},{self.street},{self.allay},{self.zipcode}"
