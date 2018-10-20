from django import forms


TIMEOUTS = (
    (900, '15 min'),
    (3600, '1 hour'),
    (21600, '6 hours'),
    (43200, '12 hours'),
    (86400, '24 hours')
)


class SheduleForm(forms.Form):
    timeout = forms.ChoiceField(label='or update every', choices=TIMEOUTS)

    timeout.widget.attrs.update({'class': 'form-control ml-3'})
