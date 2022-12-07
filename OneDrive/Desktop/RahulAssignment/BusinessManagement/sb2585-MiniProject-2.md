<table><tr><td> <em>Assignment: </em> IS601 Mini Project 2  Business Management</td></tr>
<tr><td> <em>Student: </em> Sairahul Boynapalli (sb2585)</td></tr>
<tr><td> <em>Generated: </em> 12/7/2022 12:09:35 AM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F22/is601-mini-project-2-business-management/grade/sb2585" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>checkout dev and pull any latest changes</li><li>Create a branch called MiniProject-2</li><li>Add all the baseline files first under a folder called BusinessManagement (included below)</li><li>Don't forget to copy your .env file from flask_sample into BusinessManagement</li><li>source the venv and pip install the requirements.txt</li><li>Run the BusinessManagement/sql/init_db.py script</li><li>Immediate add/commit/push to github</li><li>Open a pull request and keep it open until you're done adding the submission file</li><li>&nbsp;(optional) updated the deploy dev yml file and add MiniProject-2 so you can deploy to dev without needing to merge into dev</li><li>Make your code changes per the following requirements</li><ol><li>Important: run the test files indiviudally as you're working/testing to save on query quota usage</li></ol><li>Add/commit periodically (recommended after you implement a TODO item or checlist item)<br></li><li>Anywhere relevant add your ucid and the date you added the code (best to do this as you go)</li><li>You'll be capturing website screenshots from dev and code snippet screenshots (ensure you upload these properly as pull request comments to the pull request from step 5</li><ol><li>Note: You don't need separate screenshots for each checklist item, when possible it's recommended to try to capture multiple items together</li><li>Ensure all screenshots are properly captioned in the deliverable section</li></ol><li>You may save your progress when filling out this submission as often as you want</li><li>Once done, copy the markdown or download the md file and save it under the BusinessManagement folder</li><li>Do a final add/commit/push</li><li>Verify everything looks ok in the pull request</li><li>Merge the pull request</li><li>Make a new pull request from dev to prod and merge it</li><li>Navigate to the submission file under the BusinessManagement folder</li><li>Copy the github url to the exact file and submit it to Canvas</li></ol><div>You'll be implementing a basic Business Management site.</div><div>There will be some provided files fully working as-is and some skeleton files you'll need to fill in.</div><div>The files you need to fill in will have TODO items or comments mentioning what's expected.</div><div>There are provided test case files too that all must be passing for full credit. Do not edit these test case files.</div><div>The site will handle CRUD operations for Companies and Employees as well as allowing import of Company/Employee data via a csv file.</div><div><br></div><div>Baseline files:&nbsp;<a href="https://github.com/MattToegel/IS601/tree/F22-MiniProject-2">https://github.com/MattToegel/IS601/tree/F22-MiniProject-2</a></div><div>May want to download branch as a zip, then copy/paste the files into your repo</div><div><br></div><div>Provided files you don't need to edit:</div><div><ul><li>000_create_table_companies.sql</li><li>001_create_table_employees.sql</li><li>db.py</li><li>init_db.py</li><li>flash.html</li><li>company_dropdown.html</li><li>country_state_selector.html</li><li>upload.html</li><li>sort_filter.html</li><li>all test files</li><li>geography.py</li><li>__init__.py (remains empty)</li><li>Dockerfile</li><li>main.py</li><li>index.py</li></ul><div>All other files likely have requirements to fill in.</div></div><div><br></div></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Identity Edits and Setup </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the index page being displayed (from dev)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206072125-ee31943c-312a-40d5-bb46-a865871ede7c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Index Page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot from the DB extension of vs code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206072615-702b0d3e-d044-4592-a56d-aa2305ccf7e7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>IS601_MP2_Companies<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206072801-aeae10f5-7649-4201-82df-3d5402f192a9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>IS601_MP2_Employees table<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Upload / Import CSV File (provided data.csv) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of /import route</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206073914-bed4b2d7-a2b5-4ec9-adf2-e849dd063e3d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Data uploaded Succcess Message and How many records were processed<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206074399-829bb5f3-10a1-4759-ae23-bdd66fa3f48a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Error if it is not CSV file<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206093482-82d3e672-c11c-40d6-a91f-984d2b60dd22.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Dictionary Handling of employee and company<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of the website when uploading the data.csv file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206073914-bed4b2d7-a2b5-4ec9-adf2-e849dd063e3d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success Message and counted when data is uploaded<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206074399-829bb5f3-10a1-4759-ae23-bdd66fa3f48a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the error message when the file is not a .csv file<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206075799-1d9b463b-ea54-4e7a-a6b6-55fbc212a9ec.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> the error message when the form was submitted without a file attached<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data (basic summary/view)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206075216-084e02da-f6d3-40ef-8b50-6641a7dd46b2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Employee is added<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206076276-1b6031af-df77-4a92-be5b-6666678ea3b5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Company  is  added<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206076565-ca454a53-9d17-4460-95b0-c123b1b9f399.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>count and Amazon Audible is added in company<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206076714-2b3e7112-27ae-4ea9-a7f8-10c0bef059c8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>count and sai rohith mechineni was added to employee table and count is<br>increased to 1001<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Add Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206077242-65911bab-81ce-4ee2-849e-378bc5da7530.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>shown all inputs of add employee<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206077542-092682e3-40d4-45d6-a3d7-66e5c6f2f481.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> INSERT query<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206077807-0af55053-7785-41df-8ac8-5d6537100dab.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Except block should have a user friendly message flashed and a print() of<br>the exception<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206078175-f8dc71e5-a65b-47d5-b56a-0d70c5c602c8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>valid data prior to submissin<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206078272-65424275-98ce-456a-9694-830304bf18bd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>success message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206078837-db1ba6fa-4c30-4bd3-86b5-47ab4582a68d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>first_name error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206079016-ca885467-4113-4216-8895-16628c0d6971.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>last_name error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206079092-b5ad20d0-86c9-4efe-bdf7-b4b14eeb40ff.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>email error message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new employee DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206079336-d6913a90-d629-41ad-a395-caa6321e4770.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the valid employee data <br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> List/search Employees </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206079628-f4c240de-3cac-4a79-a904-0bab23e59e18.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>appending<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206079796-f57763f6-1284-4f79-809b-53e35dc17e99.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Select Query<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206079958-28f02ca9-0ee7-4299-978a-cc8d01152dd9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>request args for fn, ln, email, company, column, order, limit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206080197-6f838412-c679-42ba-bad0-20f8c7945606.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Limits and error messages<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206080354-21d5d282-dbb5-46eb-856c-dd7b693f8def.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Exception with proper message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206080500-fd6dc80d-7bb6-4dee-bcaa-b42824676760.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>first name<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206080647-abe3a4d8-dd4a-48d8-9564-3a4c76e83ec2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Last name<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206080740-c8652f4e-36ea-450b-a5f1-9a62890a1ef1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>email<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206080934-e0001d67-a599-4e5e-a074-5740fb237a35.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>company<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206081107-d275aafe-d4e3-414e-b8cd-21c966e7f9a9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Descending<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206081168-af3f61c1-447d-4a3a-965f-4e33ff1fb92c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Ascending<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Edit Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206081420-a28dd42c-b190-4297-a1e6-c0f4af29c8ec.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Request,first_name,last_name,company,email<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206081674-d5cfe5f3-2d82-42c4-995d-77a554ae5786.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Update Query<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206081824-f0293968-5614-4f93-9bbe-1bbb45ce4648.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Except blocks and select Query<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206081983-a374c629-0dc6-4ee3-967d-bca35ada8382.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>render_template<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206082147-551eb820-b625-4d22-91c9-5858e6ffbca6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before an edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206082290-d7a03567-8227-4c83-a84d-ce6222ecf9d5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Updated record<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206082465-942b83e1-7267-4fbc-b5ad-2d7c43637c63.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After Edited<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of employee data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206082653-777e9259-d68a-4091-b8a0-25ebb42657b6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before Edited in DB<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206082876-09cddf39-9715-4cd2-b5b5-7a4221e3ff76.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Ajith Reddy Poly is Ajith Polu in the screenshots of db<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206083062-70c47013-8545-4ddc-bb6e-c791ebd3ed74.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Add Company and name, address, city, state, country, zip, website<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206083451-1111dbdf-8944-4532-b65b-502cb20fe3d1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Insertion Query<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206083550-4a9b2778-378c-4c61-93dd-45610d7861e9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Except Block<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206083807-a9cf8b72-bc81-4663-a14e-94ae84517bc0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Company before submission<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206083914-138a8145-0730-434b-b825-3cfcb3dbbd69.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success Message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206084100-3d160bdb-adab-470c-bdcf-18cf46ccd352.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>name error<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206084213-32ba984f-2237-4fc6-8b2e-1d9483f7b4c6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Street Error<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206084304-6b291946-e79b-454c-afae-9c2438ff837b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>City Error<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206084422-0a1619c8-d26c-4c96-b565-5d63dacf740d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>State Error<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206084530-e1c2e8dd-d7ce-4806-a263-6b9614114fea.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Country Error<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new company DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206084802-cd2e7645-d322-4217-ad9d-083af11c9fe4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Valid Company record<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> List/Search Comapny </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206085209-30d57b73-57de-4197-a732-8d2e09755a7e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Select Querry<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206085319-0f405807-7f58-4781-9ada-7ebb6f3adc65.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Request args<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206085535-ca27aec9-6081-40e9-816d-b5d36bc8745d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Filters<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206085784-85e6611b-2abe-4466-b16a-b8352bac5b81.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Limits<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206085864-4f728732-d2ff-42dd-a7c2-8ec84e6eeab1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Exception<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206086018-49babb07-f711-437b-992b-4ac329c0a929.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Name filter<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206086152-4a58ec6d-4785-4cc7-bc50-f44dc61c57f8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Country Filter<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206086240-e326676b-8854-468d-9fe3-84c7b6fa0dfc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>State Filter<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206086295-2a97bbac-eeff-457e-bccd-79e3ca0ea0a4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Ascending<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206086364-46223b18-e1f0-4fc7-85c8-7024b0ffb74b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Descending<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Edit Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206086640-38b8de6a-2a91-4cc9-8128-4da1268cc13f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Request args<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206086793-35a82077-649c-4909-b13b-170b3ddcb5f1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Flasher or error messages<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206086857-55f16346-2098-4233-a684-92f254f82095.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Update Querry<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206086940-19523ff9-99b1-4fe0-baa8-e48c843535da.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Exception two blocks<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206087044-24069bd1-27e3-4126-8882-69a23dab3405.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Select Querry<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206087107-c542acd3-7f22-4bf5-ae42-9b381cd7ddea.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Render template<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206087311-e0cc0567-9d80-461d-8f5d-480efee2c52f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Data before edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206087687-3d56706e-4636-4a7f-961a-76583e465bf1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>changed to Rahul and Ajith Movers and co after edited<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of company  data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206087473-9c9da412-b78a-4cd1-a841-e8a8ce6b4aeb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Rahul Movers and co before edited<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206087880-1d10f959-3f7f-4b10-9c2e-a7134425dba7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>chnaged to Rahul and Ajith Movers and Co<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Delete Employee and Delete Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /delete route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206089206-55d221e1-adfa-468c-8952-3c2ee99bbb8c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Delete, Redirect and all request args are passed to the redirect route and<br>sucess message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after website screenshot of deleting an employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206088206-6e367b59-8e27-48ce-9fef-d7f06e65a806.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Ajith is searched as it is present<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206088290-6f375d30-a792-4d60-b462-2b61ed55bd8e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Ajith is then searched and deleted so it&#39;s not showing there is flash<br>message saying it deleted and also getting redirected to employee table<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of code for /delete route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206089545-09a60173-2546-486f-94fc-bf5473ce4ef7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Delete, Redirect and request args and success message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after website screenshot of deleting a company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206089747-a9083039-670b-4f46-b05e-60141f581cce.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before Amazon Audible Inc and <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206089881-4cff2a20-fcbf-4c66-9864-3a5ef19b1466.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After message is Amazon Audible Inc is deleted and error message  is<br>deleted  and success message after process<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Test Cases and Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot Test case Results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788939/206092351-5229b468-30b7-4eed-8c37-08d1ddd78956.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Testcases running Screenshot<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Issues / Learnings / Interesting things to note</td></tr>
<tr><td> <em>Response:</em> <p>I learnt flask, python and connecting databases handling and connecting table in html<br></p><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F22/is601-mini-project-2-business-management/grade/sb2585" target="_blank">Grading</a></td></tr></table>