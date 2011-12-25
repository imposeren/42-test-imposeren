# -*- coding: utf-8 -*-

from windmill.authoring import WindmillTestClient


def test_recordingSuite0():
    client = WindmillTestClient(__name__)
    client.click(link=u'Edit')
    client.waits.forPageLoad(timeout=u'20000')
    client.waits.forElement(link=u'Login', timeout=u'8000')
    client.click(link=u'Login')
    client.click(id=u'id_username')
    client.type(text=u'admin', id=u'id_username')
    client.type(text=u'admin', id=u'id_password')
    client.click(value=u'login')
    client.waits.forPageLoad(timeout=u'20000')

    client.waits.forElement(timeout=u'8000', id=u'id_birth')
    client.click(id=u'id_birth')
    client.click(xpath=u"//div[@id='ui-datepicker-div']/div/div/select[2]")
    client.select(xpath=u'/div/div/select[2]', option=u'1987')
    client.click(xpath=u"//div[@id='ui-datepicker-div']/div/div/select[1]")
    client.select(xpath=u'/div/div/select[1]', option=u'Dec')
    client.click(link=u'11')

    #And this should work anyway:
    client.waits.forElement(link=u'Uploading', timeout=u'8000')
    client.waits.forElement(link=u'Success!', timeout=u'8000')
