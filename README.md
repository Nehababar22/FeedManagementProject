# FeedManagementProject

1] Create Users app:

      1. Create models:
         - Model Name: User(AbstractUser)
         - Fields(All fields are mandatory):
            1. email(unique=True)
            2. first_name 	- CharField
            3.last_name 	- CharField
   
      2. Create User CRUD API
   
                1] Create/POST API
                  - Should be accessible by anyone.
                  - Assign the default Group to the user as Admin while creating every new user.

                2] Read/GET API
                   - Super User is able to see all users' details.
                   - Admin should only read his own details, write a permission which only returns Admin’s logged-in user details.
                   - Password field should be hidden.
                   - The Address should return the user's Address object with all fields.

               3] Update/PUT/PATCH API
                  - Admin should be able to update only his details.
                  - Super User can update all users' details.

               4] DELETE API
                  - Super User is able to delete all user accounts..
                  - Admin shouldn't be able to delete his/others user accounts.
        
      3. Write CRUD Unit Test cases for Users.
         - CRUD unit tests  for Super User/Admin/Anonymous users.

        
2] Write a Signal to add the default User Group as “Admin” for every new user creation.

3] Create Model Name: Group
      - Fields(All fields are mandatory):
        1.Name
      Note: Group Types will be  Admin and Manager.
      
4] Write a management command for creating groups.
   (Groups names are: Admin, Manager)


5] Create Address app:

    1. Create models: 
       - Model Name: Address
       - Fields(All fields are mandatory):
          1.street 		- CharField
          2.city 		- CharField
          3.state 		- CharField
          4.country 	- CharField
          5.user		- FK(User)
          
    2. Create Address CRUD API
            1] Create/POST API
              - Should be accessible by Authenticated User only.
              - If the request user Address has already exists, then return an error message.

            2] Read/GET API
             - Super User is able to see all address details.
             - Admin should only read his own address.

            3] Update/PUT/PATCH API
             - Admin should be able to update only his Address.
             - If an Admin tries to update any other user addresses, display an error message.
             - Super User can update all users' addresses.

            4] DELETE API
             - Super User is able to delete all user Addresses..
             - Admin shouldn't be able to delete his/others Address.
             
    3. Write CRUD Unit Test cases for Address.
        - CRUD unit tests  for Super User/Admin/Anonymous users.


6] Create Feeds app:

    1. Create models:
        - Model Name: Feed
        - Fields(All fields are mandatory):
            1. title		- CharField(max length=320)
            2. content	- TextField
            3. image		- ImageField
            4. created_by	- FK(User)
            5. created_at	- DateTimeField
            6. updated_at	- DateTimeField
            
    2.Create Feeds CRUD API:
            1] Create/POST API
               - Should be accessible by Authenticated User.
               - Set created_by user to logged-in user.

            2] Read/GET API
               - Super User is able to see all feeds details.
               - Admin should only read his own feeds, write a permission which only returns logged-in user feeds.
               - The created_by field should return user’s ID, First name, Last Name, Username, email  and group Name.

           3] Update/PUT/PATCH API
              - Admin should be able to update only his feeds.
              - If an Admin tries to update any other user feeds, display an error message.
              - Super User can update all users' feeds.

           4] DELETE API
              - Super User should be able to delete all user Feeds..
              - Admin should be able to delete his  Feeds.

    3. Write CRUD Unit Test cases for Feeds.
        - CRUD unit tests for Super User/Admin/Anonymous users.
       
    4. Download Feeds Report API.
      - Admin should be able to download their own feeds report.
      - Super User should be able to download all user feeds.
      - Anonymous users shouldn’t be able to access this API.
        (NOTE: Downloaded report should be CSV format and columns will be:
           Title, Content,Publish Date,Creator(Users firstname & lastname))
 
