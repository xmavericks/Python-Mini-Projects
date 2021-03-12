# Taking User Input for basic details
print("Enter some basic details about yourself below:- ")
# Basic Details
name = input("What is your good name?: ")
contact_number = int(input("\nWhat is your 10 digit mobile number?: "))
extension = input("\nWhat is your extension?: \n")
portfolio_url = input("\nEnter Portfolio URL: \n")
github_username = input("\nEnter github username: \n")
linkedin_url = input("\nEnter LinkedIn url: \n")
print("Enter some details about your work and experiences:- ")
# Experience related input
experience = input("\nHow many years of experience do you have ?: \n")
tools_and_tech = input("\nWhat are your tools and technologies expertize, mention all?: ")
databases = input("\nWhat are the databases have you worked on?: ")
prev_org = input("\nEnter your Previous Organization name: ")
site = input("\nEnter site name where you found this job opening opening: ")
software_role = input("\nEnter software role, eg - Software Developer, SDET etc: ")

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
    print("Thank you so much for making this opportunity available on"+site+"\n")
    print("My name is "+name+" and I am a Software Engineer with more than "+experience+" years of experience as "+software_role+"."+"During my previous employment with "+prev_org+", I have worked on several tools and technologies like - "+tools_and_tech+"with some databases experience of "+databases+"\n")
    print("As I can see that you are looking for a person who has some working experience in"+software_role+"and have some working knowledge of some programming with data structures and algorithms as well as with a good problem solving and analytical knowledge.\n")
    print("For which I want to say that, I might be a good fit for this position.")
    print("\nLooking forward to hear from you !\n")
    print("\nThanks and Regards,")
    print(name)
    print("Contact number: "+extension+" "+str(contact_number))
    print("Github: "+"https://www.github.com/"+github_username)
    print("LinkedIn: "+linkedin_url)
    print("Portfolio: "+portfolio_url)

cover_letter()
