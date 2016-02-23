from django.forms import Form


class GForm(Form):

    def __init__(self, *args, **kwargs):
        super(GForm, self).__init__(*args, **kwargs)
        for field in self:
              field.field.widget.attrs.update({
                  'ng-model': '{0}'.format(field.name),
              })
