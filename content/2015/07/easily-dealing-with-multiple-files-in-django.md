Title: Easily Dealing With Multiple Files in Django
Date: 2015-07-17 11:00
Category: Old
Tags: python, django,development
Slug: easily-dealing-with-multiple-files-in-django
Authors: easydevmixin
Summary: A method to upload multiple files with Django
Status: published

When working with Django we have a couple of fields dealing with files, FileField and ImageField. The thing is that using these fields we can only upload one file at a time so problems come when we want to upload more than one field in one request.

For this post I’m assuming that we are working with HTML5. Using it we will leverage the [multiple](http://www.w3schools.com/tags/att_input_multiple.asp) attribute for a file input. I’m also assuming you have a Django app with `urls.py` pointing to a couple of pages named `add_attachment` and `add_attachment_done`.

## The model
Say we have a class with a FileField and some other fields. E.g.:

    #!python
    # models.py
    import random
    import string
    import os

    from django.db import models
    from django.utils.timezone import now as timezone_now


    def create_random_string(length=30):
        if length <= 0:
            length = 30

        symbols = string.ascii_lowercase + string.ascii_uppercase + string.digits
        return ''.join([random.choice(symbols) for x in range(length)])


    def upload_to(instance, filename):
        now = timezone_now()
        filename_base, filename_ext = os.path.splitext(filename)
        return 'my_uploads/{}_{}{}'.format(
            now.strftime("%Y/%m/%d/%Y%m%d%H%M%S"),
            create_random_string(),
            filename_ext.lower()
        )


    class Attachment(models.Model):
        parent_id = models.CharField(max_length=18)
        file_name = models.CharField(max_length=100)
        attachment = models.FileField(upload_to=upload_to)


It’s worth noting we are not storing the file given by the user with the same name, but with a random one. This is done in order to avoid specially crafted file names attacks. The origininal file name is stored in the database.

## The HTML
Once we have that class we can create a HTML5 form for it. Take into account we are not using the field file\_name from the model. This is because there will be multiple files, so there is no point asking the name for a single file.

    #!html5
    <!-- add_attachment.html -->
    <!DOCTYPE html>
    {% load i18n staticfiles %}
    <html>
    <!-- file: add_attachment.html -->
        <head lang="en">
            <meta charset="UTF-8">
            <title>{% block title %}{% endblock %}</title>
        </head>
        <body>
            <form action="" method="post" enctype="multipart/form-data">
                {% csrf_token %}
                <p>
                    <label for="id_parent_id">Parent ID:</label>
                    <input id="id_parent_id" type="text" maxlength="18" name="parent_id">
                </p>
                <input type="file" name="myfiles" multiple>
                <button type="submit">{% trans "Save" %}</button>
            </form>
        </body>
    </html>

## The view
Finally we have the view. The view is just a function that will process the POST request saving the files and then redirect to the `add_attachment_done` page. If the request is not a POST, it will render the page `add_attachment.html`.

What the view does is just taking the value of `myfiles` input value, which will be an array of files. Then, for each file creates a new `Attachment` with the specified fields and, finally, saves the attachment to the database. This means there will be an entry to the attachments table and the file wherever you set the media files on your settings.

    #!python
    # views.py
    # -*- coding: utf-8 -*-
    from django.shortcuts import redirect, render
    from django.shortcuts import render_to_response

    from .models import Attachment


    def add_attachment(request):
        if request.method == "POST":
            parent_id = request.POST['parent_id']
            files = request.FILES.getlist('myfiles')
            for a_file in files:
                instance = Attachment(
                    parent_id=parent_id,
                    file_name=a_file.name,
                    attachment=a_file
                )
                instance.save()

            return redirect("add_attachment_done")

        return render(request, "add_attachment.html")


    def add_attachment_done(request):
        return render_to_response('add_attachment_done.html')

## Conclusion
This will process all files included in the previous form and save them where it has been established by the `upload_to` method on models.py.

Although a short post, I hope you find it useful. On another post I will add Ajax to the process, so everything will look smoother.

Happy multiple file uploading!

**Update 2016/10/19**: Today I’ve received an email about this post in which this solution was not working with Django 1.9. I have created a dummy project containing this code so you can use it as a template for your own code. You can find it here [https://github.com/easydevmixin/multiple_files](https://github.com/easydevmixin/multiple_files)
