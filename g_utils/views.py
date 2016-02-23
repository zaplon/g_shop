from django.shortcuts import render, render_to_response, RequestContext, HttpResponse
import importlib
import json


def render_form(request):
    from django.conf import settings
    print settings.TEMPLATE_DIRS
    data = request.POST
    class_data = data['class'].split(".")
    module_path = ".".join(class_data[:-1])
    class_str = class_data[-1]
    module = importlib.import_module(module_path)
    # Finally, we retrieve the Class
    form = getattr(module, class_str)
    if 'form_data' in data:
        print data['form_data']
        form = form(data=json.loads(data['form_data']))
        if form.is_valid():
            form.save()
        return HttpResponse(content=form.errors.as_json(), content_type='application/json')
    else:
        form = form()
    return render_to_response('g_utils/form.html', {'form': form}, context_instance=RequestContext(request))
