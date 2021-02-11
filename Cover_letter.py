t_and_t = input("Enter Tools and Technologies on which you have worked: ")
name = input("Enter your good name: ")
experience = input("Enter your Work Experience: ")
databases = input("Enter database names on which you have worked: ")
prev_org = input("Enter your Previous Organization name: ")
site = input("Enter site name where you found this opening: ")
software_role = input("Enter software role, eg - Software Developer, SDET etc: ")
contact_number = int(input("Enter contact number: "))
github_username = input("Enter github username: ")

#cover_dict = {}

def cover_letter():
    #inserting name
    # if "Name" in cover_dict:
    #     cover_dict["Name"].append(name)
    # else:
    #     cover_dict["Name"] = [name]
    # #Inserting Languages    
    # if "Languages" in cover_dict:
    #     cover_dict["Languages"].append(languages)
    # else:
    #     cover_dict["Languages"] = [languages]
    # #Inserting Previous Organization    
    # if "prev_org" in cover_dict:
    #     cover_dict["prev_org"].append(prev_org)
    # else:
    #     cover_dict["prev_org"] = [prev_org]
    # #Inserting Experience    
    # if "experience" in cover_dict:
    #     cover_dict["experience"].append(experience)
    # else:
    #     cover_dict["experience"] = [experience]
    # #Inserting Databases    
    # if "databases" in cover_dict:
    #     cover_dict["databases"].append(databases)
    # else:
    #     cover_dict["databases"] = [databases]
    # # Inserting Site
    # if "site" in cover_dict:
    #     cover_dict["site"].append(site)
    # else:
    #     cover_dict["site"] = [site]
    # # Inserting Role
    # if "software_role" in cover_dict:
    #     cover_dict["software_role"].append(software_role)
    # else:
    #     cover_dict["software_role"] = [software_role]
    # # Inserting Contact number
    # if "contact" in cover_dict:
    #     cover_dict["contact"].append(contact_number)
    # else:
    #     cover_dict["contact"] = [contact_number]
    # # Inserting GitHub Username
    # if "github_username" in cover_dict:
    #     cover_dict["github_username"] = [github_username]
    # else:
    #     cover_dict["github_username"] = [github_username]
    
    # Printing output
    print("Dear Hiring Person,\n")
    print("Thank you so much for making this opportunity available on", site,"\n")
    print("My name is ",name," and I am a Software Engineer with more than ",experience, " of experience as "+software_role+"."+"During my previous employment with "+prev_org+", I have worked on several tools and technologies like,"+t_and_t+" with some databases experience of, "+databases)
    print("As I can see that you are looking for a person who has some working experience in",software_role)
    print("For that I want to say that, I might be a good fit for this role.")
    print("\nLooking forward to hear from you !\n")
    print("\nThanks and Regards,")
    print(name)
    print("Contact number: "+str(contact_number))
    print("Github: "+"https://www.github.com/"+github_username)

cover_letter()
