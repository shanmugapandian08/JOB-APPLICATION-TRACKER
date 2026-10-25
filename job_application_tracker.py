
#Menu creation
print("==== JOB APPLICATION TRACKER ====\n\n","1.Add Application\n","2.View Application\n","3.Update Application\n","4.Delete Application\n"
,"5.Search Application\n","6.Dashboard\n","7.clear\n","8.History\n","9.Exit")
add_application=[]
history=[]
s=0
while s<1:
    try:
        menu=int(input("Enter the number from menu :"))

        if(menu == 1): 
          def add_app(name,role,location,status,date):
              app_dict={"Company Name":name, 
                      "Job Role":role,
                      "Location":location,
                      "Apply Date":date,
                      "Status":status
                      }
              append=True
              for ite in add_application:
                  if app_dict["Company Name"]== ite["Company Name"]:
                      print("Already Applied")
                      append=False
                      break

              if append :
                add_application.append(app_dict)
                print()
                print("Application added successfully")

          name=str(input("Enter the Company Name :")).title()
          role=str(input("Enter the Job Role :")).title()
          location=str(input("Enter the Location :")).title()
          status=str(input("Enter the Status :")).title()
          date=str(input("Enter the  Apply Date :")).title()

          add_app(name,role,location,status,date)

        elif(menu == 2):
            if (len(add_application)!=0):
                for view in add_application:
                    print(view)
                    print()
            else:
                 print("No Application Found !!!")
            print(len(add_application),"- Application Applied")

        elif(menu == 3):
            not_found=0
            company_name=str(input("Enter the Company Name for Update :")).title()
            for update in add_application:
                if update["Company Name"]== company_name:
                    not_found=1

                    print("What do you Want to Update ? \n 1. Job Role \n 2. Location \n 3. Apply Date \n 4. Status")
                    what_update=int(input("Enter what do you want to update ?"))
                    if(what_update == 1):
                        new_jobrole=str(input("Enter the new Job Role :")).title()
                        update["Job Role"]= new_jobrole
                    elif(what_update == 2):
                        new_Location=str(input("Enter the new Location :")).title()
                        update["Location"]= new_Location
                    elif(what_update == 3):
                        new_Applydate=str(input("Enter the new Apply Date :")).title()
                        update["Apply Date"]= new_Applydate
                    elif(what_update == 4):
                        new_status=str(input("Enter the new Status :")).title()
                        update["Status"]=new_status

                    print("Updated Successfully")
                    break
            if not_found !=1:
                print("No Company Name Found!!!")

        elif(menu == 4):
            delete=str(input('Enter the type of deletion [ Name / Status ]')).title()
            if delete == "Name":
                del_name=str(input("Enter the Name to delete :")).title()
                not_found=True
                for delt in add_application:
                    if del_name==delt["Company Name"]:
                        indx=add_application.index(delt)
                        history.append(delt)
                        add_application.pop(indx)
                        print(" Application Successfully Deleted...")
                        not_found=False
                        break
                if not_found:
                    print("can't find anything like this Company Name")

            elif delete == "Status":
                del_status=str(input('Enter the Status to delete :')).title()
                not_found=True
                for delt_stat in add_application:
                    if del_status == delt_stat["Status"]:
                        stat_indx=add_application.index(delt_stat)
                        history.append(delt_stat)
                        add_application.pop(stat_indx)
                        print(" Application Successfully Deleted...")
                        not_found=False
                        break
                if not_found:
                    print("can't find anything like this status name")
            else:
                print("Wrong Deletion Method please check")

        elif(menu == 5):
            not_in_srch=True
            search=str(input("You can search application by using[Company Name / Job Role / Location / Apply Date / Status ] :")).title()
            for srch in add_application:
                keys=srch.keys()
                keys=list(keys)
                for insrch in keys:
                    if (search == add_application[add_application.index(srch)][insrch]):
                        not_in_srch=False
                        print(srch)
                        break
            if not_in_srch:
                print("Search not found!")

        elif(menu == 6):
            appl_ied=0
            inter_view=0
            sele_cted=0
            reje_cted=0

            for dash in range(len(add_application)):
                if add_application[dash]['Status']== "Applied":
                    appl_ied+=1
                elif add_application[dash]['Status']== "Interview":
                    inter_view+=1
                elif add_application[dash]['Status']== "Selected":
                    sele_cted+=1
                elif add_application[dash]['Status']== "Rejected":
                    reje_cted+=1
                else:
                    pass
            print("\t\t\t\t\t\t==========Dash Board==========\n")
            print("\t\t\t\t\t\tTotal Application :",len(add_application))
            print()
            print()
            print("\t\t\t\t\t\tApplied :",appl_ied)
            print()
            print("\t\t\t\t\t\tInterview :",inter_view)
            print()
            print("\t\t\t\t\t\tSelected :",sele_cted)
            print()
            print("\t\t\t\t\t\tRejected :",reje_cted)
            print()
            print("\t\t\t\t\t\t==============================")

        elif(menu==7):
            if len(add_application) > 0:
                history=add_application.copy()
                add_application.clear()
                print("cleared")
            else:
                print("Nothing to clear")

        elif(menu==8):
            print("----------------History----------------------")
            
            print()
            if len(history)>0:
                print(history)
            else:
                print("No previous History")

        elif(menu==9):
            break

        else:
            print("wrong menu number please check")
        print()




    except Exception:
        print()
        print('You can only enter number for selection...')
        print()
        continue
