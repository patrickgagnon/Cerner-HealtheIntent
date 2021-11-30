# Cerner-HealtheIntent
HealtheIntent open development services allow access to population health concepts using RESTful APIs. 

>[HealtheIntent Documentation](https://docs.healtheintent.com/)

This repository contains a Python wrapper for a number of Cerner Open Code APIs
1. Cerner Data Syndication API - https://docs.healtheintent.com/api/v1/data_syndication/
2. Organizations API - https://docs.healtheintent.com/api/v1/organization/
3. Personnel API - https://docs.healtheintent.com/api/v1/personnel/


## Subclass Definitions

### Feeds aka Data Syndication

1. **Feeds**
: The set of data that you want to receive on a schedule, for example, Longitudinal Record for population ABC.

2. **Channels**
: Specifies that you want to receive a feed’s bundles using a particular channel type and provides any necessary configuration for the channel type. For example, a channel could specify that you want to receive your Longitudinal Record for Population ABC feed using the DOWNLOAD channel type.

2. **Bundles**
: The output of a feed, for example, Changes to the Longitudinal Record for population ABC between 2018-04-01 and 2018-04-02.

3. **Deliveries**
: The status of delivering a particular bundle using a particular channel. For example, you would use the Deliveries endpoint to determine whether the archive file for changes to the Longitudinal Record for population ABC between 2018-04-01 and 2018-04-02 bundle is available for you to download.

### Organization

1. **Location**
: A location represents a physical place with a single physical address, for example, a laboratory facility, practice site, hospital, or even a department within a hospital associated with an organization. Currently, personnel organizations and locations are not related in the API, but they will be in the future.

2. **Organization**
: A formally or informally recognized group of people or organizations formed for the purpose of achieving a collective action, for example, companies, institutions, corporations, departments, community groups, and health care practice groups.

3. **Organization Group**
: Organization groups are sets of organizations that are grouped for a common purpose. For example, organizations can be grouped to apply a consistent scoring methodology across organizations of the same type, filter a report to a certain set of organizations, or display a group of organizations together in applications.

### Personnel

1. **Personnel**
: Personnel are the people involved in the health care of a population. In most cases, personnel are employees or affiliates of a health care system or provider.
: Users are personnel who log in to HealtheIntent applications. All users must be personnel, but not all personnel are necessarily users. Users gain access to features and information in HealtheIntent applications through membership in personnel groups and by being a member or administrator of organizations.

2. **Personnel and Organization Relationship**
: A personnel can be a member or administrator of an organization, and some personnel may be both members and administrators of the same organization. Organization members typically are personnel who provide health care services to patients and whose financial performance and quality metrics contribute to the overall performance of the organization. Administrators are personnel who monitor and manage the activities and performance of their organizations.

3. **Personnel Group**
: Personnel groups are sets of personnel who are grouped together to give them access to the same features or information. A personnel can belong to as many or as few personnel groups as necessary.

#### URL Structure
>https://{tenant}.api.{region}.healtheintent.com/{api}/{version}/{resource}

# Prerequisites
A settings.py file is required for this wrapper to work. This file should contain the variable BEARER_HEADER as the Authorization Bearer header.

# Installation 
```
!pip install Cerner-HealtheIntent
```
# Import
```
import healthetintentAPI as h
```
# Usage
```
o = h.Organization()
print(o.get_organization())
```
```
p = h.Personnel()
print(p.get_personnel())
```



