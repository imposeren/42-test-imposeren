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

    client.click(id=u'id_birth')
    #next lines realy work only just for some datepicker example site
    #TODO: change to something real
    client.click(xpath=u'/html/body/div[11]/div/div[2]/div/div/select[2]')
    client.select(xpath=u'/div/div[2]/div/div/select[2]', option=u'1987')
    client.click(xpath=u'/html/body/div[11]/div/div[2]/div/div/select[1]')
    client.select(xpath=u'/div/div[2]/div/div/select[1]', option=u'December')
    client.click(
        xpath=u'/html/body/div[11]/div/div[2]/div/table/tbody/tr[2]/td[4]/a')
    client.click(name=u'submit')

    #And this should work anyway:
    client.waits.forElement(link=u'Uploading', timeout=u'8000')
    client.waits.forElement(link=u'Success!', timeout=u'8000')
