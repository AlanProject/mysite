#!/usr/bin/env python
#-*- coding:utf-8 -*-

from django import forms
from django.core.exceptions import ValidationError

class UserInfo(forms.Form):
    name = forms.CharField(label='用户名',error_messages={'required':u'用户名不能为空'},
                           widget=forms.TextInput(attrs={'class':'form-control','placeholder':u'用户名'})
                           )



import re


    # user_type = (
    #     ('0',u'普通用户'),
    #     ('1',u'超级用户')
    # )
    # passwd = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    #
    # email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':u'Email'}))

    # describe = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control','placeholder':u'描述'}),
    #                              )
    # user_choice = forms.CharField(widget=forms.Select(attrs={'class':'form-control','placeholder':u'xx'},
    #                                                   choices=user_type,
    #                                                   ))
#     mobile = forms.CharField(validators=[mobile_validate,],
#                              widget=forms.TextInput(attrs={'class':'form-control'})
#                              )
# def mobile_validate(value):
#     mobile_re = re.compile(r'^(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$')
#     if not mobile_re.match(value):
#         raise ValidationError('手机格式错误')