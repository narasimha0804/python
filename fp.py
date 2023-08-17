import os
import win32com.client

# Set the path to the folder where you want to save the attachments
save_folder = "C:/Users/nbanda.SPC/Desktop/handbook"

# Create an instance of the Outlook application
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

# Choose the folder where the attachments are located
folder = outlook.GetDefaultFolder(6).Folders("Handbook")

# Loop through each item in the folder
for item in folder.Items:
    # Check if the item has any attachments
    if item.Attachments.Count > 0:
        # Loop through each attachment
        for attachment in item.Attachments:
            # Save the attachment to the specified folder
            attachment.SaveAsFile(os.path.join(save_folder, attachment.FileName))
