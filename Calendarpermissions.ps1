#$Session = New-PSSession -ConfigurationName Microsoft.Exchange -ConnectionUri https://outlook.office365.com/powershell-liveid/ -Credential $UserCredential -Authentication Basic -AllowRedirection
#Import-PSSession $Session

Clear-Host
#Install-Module -Name ExchangeOnlineManagement
connect-ExchangeOnline -UserPrincipalName nbanda@flagshipinc.com

Get-MailboxFolderPermission itexeccalendar@flagshipinc.com:\calendar

Add-MailboxFolderPermission -identity itexeccalendar@flagshipinc.com:\calendar -user tdenisco@flagshipinc.com -AccessRights PublishingAuthor

Remove-MailboxFolderPermission -Identity execoperationscalendar@flagshipinc.com:\calendar -user "tdenisco@flagshipinc.com" -Confirm:$false

(Get-DistributionGroupMember "dfwhr").Count   


Disconnect-ExchangeOnline 

Install-Module -Name ExchangeOnlineManagement -RequiredVersion 2.0.6-Preview5 -AllowPrerelease

Get-ManagementRoleAssignment -Role “ApplicationImpersonation” -GetEffectiveUsers

#connect-ExchangeOnline -UserPrincipalName narasimha@flagshipinc.com
