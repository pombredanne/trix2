#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file has been automatically generated.
# Instead of changing it, create a file called import_helper.py
# and put there a class called ImportHelper(object) in it.
#
# This class will be specially casted so that instead of extending object,
# it will actually extend the class BasicImportHelper()
#
# That means you just have to overload the methods you want to
# change, leaving the other ones inteact.
#
# Something that you might want to do is use transactions, for example.
#
# Also, don't forget to add the necessary Django imports.
#
# This file was generated with the following command:
# manage.py dumpscript trix_core
#
# to restore it, run
# manage.py runscript module_name.this_script_name
#
# example: if manage.py is at ./manage.py
# and the script is at ./some_folder/some_script.py
# you must make sure ./some_folder/__init__.py exists
# and run  ./manage.py runscript some_folder.some_script

from django.db import transaction

class BasicImportHelper(object):

    def pre_import(self):
        pass

    # You probably want to uncomment on of these two lines
    # @transaction.atomic  # Django 1.6
    # @transaction.commit_on_success  # Django <1.6
    def run_import(self, import_data):
        import_data()

    def post_import(self):
        pass

    def locate_similar(self, current_object, search_data):
        # You will probably want to call this method from save_or_locate()
        # Example:
        #   new_obj = self.locate_similar(the_obj, {"national_id": the_obj.national_id } )

        the_obj = current_object.__class__.objects.get(**search_data)
        return the_obj

    def locate_object(self, original_class, original_pk_name, the_class, pk_name, pk_value, obj_content):
        # You may change this function to do specific lookup for specific objects
        #
        # original_class class of the django orm's object that needs to be located
        # original_pk_name the primary key of original_class
        # the_class      parent class of original_class which contains obj_content
        # pk_name        the primary key of original_class
        # pk_value       value of the primary_key
        # obj_content    content of the object which was not exported.
        #
        # You should use obj_content to locate the object on the target db
        #
        # An example where original_class and the_class are different is
        # when original_class is Farmer and the_class is Person. The table
        # may refer to a Farmer but you will actually need to locate Person
        # in order to instantiate that Farmer
        #
        # Example:
        #   if the_class == SurveyResultFormat or the_class == SurveyType or the_class == SurveyState:
        #       pk_name="name"
        #       pk_value=obj_content[pk_name]
        #   if the_class == StaffGroup:
        #       pk_value=8

        search_data = { pk_name: pk_value }
        the_obj = the_class.objects.get(**search_data)
        #print(the_obj)
        return the_obj


    def save_or_locate(self, the_obj):
        # Change this if you want to locate the object in the database
        try:
            the_obj.save()
        except:
            print("---------------")
            print("Error saving the following object:")
            print(the_obj.__class__)
            print(" ")
            print(the_obj.__dict__)
            print(" ")
            print(the_obj)
            print(" ")
            print("---------------")

            raise
        return the_obj


importer = None
try:
    import import_helper
    # We need this so ImportHelper can extend BasicImportHelper, although import_helper.py
    # has no knowlodge of this class
    importer = type("DynamicImportHelper", (import_helper.ImportHelper, BasicImportHelper ) , {} )()
except ImportError as e:
    if str(e) == "No module named import_helper":
        importer = BasicImportHelper()
    else:
        raise

import datetime
from decimal import Decimal
from django.contrib.contenttypes.models import ContentType

try:
    import dateutil.parser
except ImportError:
    print("Please install python-dateutil")
    sys.exit(os.EX_USAGE)

def run():
    importer.pre_import()
    importer.run_import(import_data)
    importer.post_import()

def import_data():
    # Initial Imports

    # Processing model: User

    from trix.trix_core.models import User

    trix_core_user_1 = User()
    trix_core_user_1.password = u'pbkdf2_sha256$12000$akVvyGIzv5mu$u1ds2n9HivKsZh/wee0SZaf5u9rkmIhG/mp+j+zVSLI='
    trix_core_user_1.last_login = dateutil.parser.parse("2014-06-12T12:45:27.876570+00:00")
    trix_core_user_1.is_active = True
    trix_core_user_1.is_admin = True
    trix_core_user_1.email = u'grandma@example.com'
    trix_core_user_1 = importer.save_or_locate(trix_core_user_1)

    # Processing model: Tag

    from trix.trix_core.models import Tag

    trix_core_tag_1 = Tag()
    trix_core_tag_1.tag = u'inf1000'
    trix_core_tag_1.category = u'c'
    trix_core_tag_1 = importer.save_or_locate(trix_core_tag_1)

    trix_core_tag_2 = Tag()
    trix_core_tag_2.tag = u'var2014'
    trix_core_tag_2.category = u'p'
    trix_core_tag_2 = importer.save_or_locate(trix_core_tag_2)

    trix_core_tag_3 = Tag()
    trix_core_tag_3.tag = u'host2014'
    trix_core_tag_3.category = u'p'
    trix_core_tag_3 = importer.save_or_locate(trix_core_tag_3)

    trix_core_tag_4 = Tag()
    trix_core_tag_4.tag = u'host2013'
    trix_core_tag_4.category = u'p'
    trix_core_tag_4 = importer.save_or_locate(trix_core_tag_4)

    # Processing model: Course

    from trix.trix_core.models import Course

    trix_core_course_1 = Course()
    trix_core_course_1.course_tag = trix_core_tag_1
    trix_core_course_1.active_period = trix_core_tag_2
    trix_core_course_1 = importer.save_or_locate(trix_core_course_1)

    trix_core_course_1.admins.add(trix_core_user_1)

    # Processing model: Assignment

    from trix.trix_core.models import Assignment

    trix_core_assignment_1 = Assignment()
    trix_core_assignment_1.unique_string = u'luring'
    trix_core_assignment_1.title = u'Hello World'
    trix_core_assignment_1.text = u'Print hello world in the terminal.'
    trix_core_assignment_1.solution = u'public class HelloWorld {\r\n    public static void main(String [] args) {\r\n        System.out.println("Hello World!");\r\n    }\r\n}'
    trix_core_assignment_1 = importer.save_or_locate(trix_core_assignment_1)

    trix_core_assignment_1.tags.add(trix_core_tag_1)
    trix_core_assignment_1.tags.add(trix_core_tag_2)

    # Processing model: Permalink

    from trix.trix_core.models import Permalink


