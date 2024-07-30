release={
       'Python 1.4':{'date':'1996-10-25',
             'description':'Functional programming tools(lamda,map,filter and reduce) \n\t\t\t\t support for complex numbers \n\t\t\t\t Function with keyword arguments',
             'renotes':''},
       'Python 2.0':{'date':'2000-10-16',
                'description':'List comprehension \n\t\t\t\t Cycle detecting garbage collector \n\t\t\t\t Support for unicod.unification of datatypes and classes',
                'renotes':'python 3.8 is a long-term supportrelease,which means that it will be supported with security updates and bug fixes until october 2024.\n python 3.8 includes a number of new features and improvements.\nIncluding:Assignment expressions.\n Positional only arguments.\nvector call optimization.\nFaster memory allocation.\nImproved performance of pickling and unpickling a number of bug fixes and security updates.\n Here are some of the new features in python 3.8:\nAssignment expression.\nAssignment expression are a new way to assign values to variables in python.They are similar to the walrus operator in perl and the assignment expression in javascript.\nAssignment expressions can be used to simplify code and make it more readable\n'},
       'Python 3.0':{'date':'2008-12-03',
                'description':'Backward incpatible \n\t\t\t\t Print keyword changed to print()function \n\t\t\t\t Raw input function depreciated',
                'renotes':' '},
       'python 3.8':{'date':'2019-10-14',
                'description':'Assignment expression \n\t\t\t\t Positional only parameters \n\t\t\t\t parallel filesystem cache for compiled bytecode files',
                'renotes':' '},
       'Python 3.9':{'date':'2020-10-05',
                'description':'Dictionary merge and update operators \n\t\t\t\t New removeprefix() and removesuffix() string methods \n\t\t\t\t Builtin generic types',
                'renotes':' '}
}
def all_release():
    if release:
        print("Existing releases:")
        print("Version\t\t Release date\t\t Description")
        print("__________________________________________________________________________________________________________")
        for version,data in release.items():
          
            print("%s\t%s\t%s"%(version,data['date'],data['description']))
    else:
            print("no releases")
            
def update():
    version=input("enter the version number to be updated")
    if version in release:
        date=input("enter new release date:")
        description=input("enter new release description:")
        if date:
            release[version]['date']=date
        if description:
            release[version]['description']=description
        print(f"{version} updated successfully")
    else:
        print(f"{version} doesn't exist")
 
def create():
    version=input("enter version number to schedule:")
    if version not in release:
        date=input("enter release date(YYYY-MM-DD):")
        description=input("enter release description:")
        renotes=input("enter the notes for the version")
        release[version]={'date':date,'description':description,'renotes':renotes}
        print(f"release{version} schedules successfully for {date}")
    else:
        print("release {version} already exists")
        

def generate():
    version=input("enter version number to generate the notes:")
    if version in release:
        print(f"version{version}")
        print(f"release notes:{release[version]['renotes']}")  
    else:
        print(f"release{version} does not exist")    
        
def view_version():
    if release:
        print("versions present in python")
        for version in release:
            print(version)
    else:
            print("no releases found.")
            
def view_version_info():
    version=input("enter the version who's information is required ")
    if version in release:
        print(f"version:{version}")
        print(f"date:{release[version]['date']}")
        print(f"description:{release[version]['description']}")
        print(f"notes:{release[version]['renotes']}")
    else:
        print(f"release {version} does not exist")

while True:
    print("1.view all releases \n 2.update \n 3.create \n 4.genetare \n release notes \n 5.view all versions \n 6.view version info \n 7.exit")
    ch=int(input("enter your choice"))
    if ch==1:
        all_release()
    elif ch==2:
        update()
    elif ch==3:
        create()
    elif ch==4:
        generate()  
    elif ch==5:
        view_version()
    elif ch==6:
        view_version_info()  
    elif ch==7:
        break
    else:
        print("wrong choice.. Try again")
        
