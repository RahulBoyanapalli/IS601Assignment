import io
from flask import Blueprint, render_template, request, redirect, flash
from werkzeug.utils import secure_filename
from sql.db import DB
import traceback
import pandas as pd

admin = Blueprint("admin", __name__, url_prefix="/admin")


@admin.route("/import", methods=["GET", "POST"])
def importCSV():
    if request.method == "POST":
        if "file" not in request.files:
            return redirect(request.url)
        file = request.files["file"]
        # print(pd.read_csv(file))
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == "":
            flash("No selected file", "warning")
            return redirect(request.url)
        # TODO importcsv-1 check that it's a .csv file, return a proper flash message if it's not
        if file and secure_filename(file.filename):
            companies = []
            employees = []
            company_query = """
            INSERT INTO IS601_MP2_Companies (name, address, city, country, state, zip, website)
                        VALUES (%(company_name)s, %(address)s, %(city)s, %(country)s, %(state)s, %(zip)s, %(web)s)
                        ON DUPLICATE KEY UPDATE address = %(address)s, city = %(city)s, country=%(country)s, state=%(state)s, zip=%(zip)s, website=%(web)s 
            """
            employee_query = """
             INSERT INTO IS601_MP2_Employees (first_name, last_name, email, company_id)
                        VALUES (%(first_name)s, %(last_name)s, %(email)s, (SELECT id FROM IS601_MP2_Companies WHERE name = %(company_name)s LIMIT 1))
                        ON DUPLICATE KEY UPDATE first_name=%(first_name)s, last_name = %(last_name)s, email = %(email)s, company_id = (SELECT id FROM IS601_MP2_Companies WHERE name = %(company_name)s LIMIT 1)
            """
            # Note: this reads the file as a stream instead of requiring us to save it
            # stream = io.TextIOWrapper(file.stream._file, "UTF8", newline=None)
            # TODO importcsv-2 read the csv file stream as a dict
            files = pd.read_csv(file)
            print(files)
            for row in files.iterrows():
                print(row)  # example
                dict1 = row[1].to_dict()
                company_row = [
                    "company_name",
                    "address",
                    "city",
                    "country",
                    "state",
                    "zip",
                    "web",
                ]
                Dict = {}
                for k in dict1.keys() & set(company_row):
                    Dict[k] = dict1[k]
                companies.append(Dict)

                employee_rows = ["first_name", "last_name", "email", "company_name"]
                Dict1 = {}
                for k in dict1.keys() & set(employee_rows):
                    Dict1[k] = dict1[k]
                employees.append(Dict1)
                pass

            if len(companies) > 0:
                print(f"Inserting or updating {len(companies)} companies")
                try:
                    result = DB.insertMany(company_query, companies)
                    print("Done")
                    # TODO importcsv-5 display flash message about number of companies inserted
                    flash(f"Inserted {len(companies)} companies records successfully!", "success")
                except Exception as e:
                    traceback.print_exc()
                    flash("There was an error loading in the csv data", "danger")
            else:
                # TODO importcsv-6 display flash message (info) that no companies were loaded
                flash("No companies records were loaded", "danger")

            if len(employees) > 0:
                print(f"Inserting or updating {len(employees)} employees")
                try:
                    result = DB.insertMany(employee_query, employees)
                    print("Done")
                    # TODO importcsv-7 display flash message about number of employees loaded
                    flash(f"Inserted {len(employees)} employees records successfully!", "success")
                except Exception as e:
                    traceback.print_exc()
                    flash("There was an error loading in the csv data", "danger")
            else:
                # TODO importcsv-8 display flash message (info) that no companies were loaded
                flash("No employees records were loaded", "danger")
    return render_template("upload.html")
