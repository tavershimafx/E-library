View:

def upload(request):
    if request.method == "POST":
        form = UploadForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            resourceupload = form.save(commit=False)
            resourceupload.uploadedBy = request.user
            resourceupload.upload_date = timezone.now()
            resourceupload.save()
            return redirect('course', pk=resourceupload.course.pk)
    else:
        form = UploadForm()
    return render(request, 'main/upload.html', {'form': form})

Associated Template:



<form method="POST" enctype="multipart/form-data" class="post-form">
            {% csrf_token %}
            <table>
                <tr>
                    <td>{{ form.title.label_tag }}</td>
                    <td>{{ form.title }}</td>
                </tr>
                <!--<tr>
                    <td>{{ form.major.label_tag }}</td>
                    <td id="majorcs" >{{ form.major }}</td>
                </tr>-->
                <tr>
                    <td>{{ form.course.label_tag }}</td>
                    <td id="coursejs">{{ form.course }}</td>
                    <td>
                      <button type="button" onclick="window.document.location='{% url "addcourse" %}'"}>Add Course</button>
                    </td>
                </tr>
                <tr>
                    <td>{{ form.resourcetype.label_tag }}</td>
                    <td>{{ form.resourcetype }}</td>
                </tr>
                <tr>
                    <td>{{ form.resourcefile.label_tag }}</td>
                    <td>{{ form.resourcefile }}</td>
                </tr>
            </table>
            <button type="submit" class="save btn btn-blog pull-right">SAVE</button>
        </form>

template for resource download:
               {% for res in resources%}
                <tr>
                    <th scope="row">{{res.resourcetype}}</th>
                    <td>{{res.title}}</td>
                    <td>{{res.uploadedBy}}</td>
                    <td><a href="{{res.resourcefile.url}}">download</a></td>
                </tr>
                {% endfor %}

display pdf FILES

def home(request):
image_data = open(“/path/to/my/image.pdf”, “rb”).read()
return HttpResponse(image_data, mimetype=”application/pdf”)

a better alternative:

from django.http import FileResponse, Http404

def pdf_view(request):
    try:
        return FileResponse(open('foobar.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()

call a view in an html:
<a target="_blank" 
    class="btn btn-info pull-right" 
    href="{% url YOUR_VIEW column_3_item.pk %}/?next={{column_3_item.link_for_item|urlencode:''}}">
    Check It Out
</a>

def YOUR_VIEW_DEF(request, pk):
    YOUR_OBJECT.objects.filter(pk=pk).update(views=F('views')+1)
    return HttpResponseRedirect(request.GET.get('next')))

<form action='actionUrl' method='GET'>
<button type='submit'> sort me</button>
</form>

from django.urls import path

from . import views

urlpatterns = [
    path(actionUrl, views.yourSort),
]

<a href="{{ pdf.PDF.url }}" target="_new">

            <td><form action='pdf_view' method='GET'>
                <button type='submit'>View</button>
            </form></td>


       <object data="/dlapp{{hld.holding.url}}" type="application/pdf" width="750px" height="750px">
          <embed src="{{hld.holding.url}}" type="application/pdf">
              <p>This browser does not support PDFs. Please download the PDF to view it: <a href="{{hld.holding.url}}">Download PDF</a>.</p>
          </embed>
      </object>



            <object data="/dlapp{{hld.holding.url}}" type="application/pdf" width="750px" height="750px">
        <embed src="/dlapp{{hld.holding.url}}" type="application/pdf">
        <p>This browser does not support PDFs. Please download the PDF to view it: <a href="/dlapp{{hld.holding.url}}">Download PDF</a>.</p>
    </embed>


    <object data="../pdf/sample-3pp.pdf#page=2" type="application/pdf" width="100%" height="100%">
<iframe src="../pdf/sample-3pp.pdf#page=2" style="border: none;" width="100%" height="100%">
This browser does not support PDFs. Please download the PDF to view it: 
<a href="../pdf/sample-3pp.pdf">Download PDF</a>
</iframe>
</object>
      </object>


      <object data="/dlapp{{hld.holding.url}}" type="application/pdf" width="750px" height="750px">
        <embed src="/dlapp{{hld.holding.url}}" type="application/pdf">
        <p>This browser does not support PDFs. Please download the PDF to view it: <a href="/dlapp{{hld.holding.url}}">Download PDF</a>.</p>
        </embed>
      </object> ------ok


    <h4>
        <table>
    {% for post in results %}
        <tr>
            <th scope="row">{{post.category}}</th>
            <td>{{post.title}}</td>
            <td><a href="{% url 'dlapp:pdf_view' %}" target="_new">View</a></td>
            <td><a href="/dlapp{{post.holding.url}}" class="btn-btn-primary">Download</a></td>
        </tr>
        </table>
      </h4>


       {% for hld in holdings %}