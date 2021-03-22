# -*- coding: utf-8 -*-

# This file is intented to test the tags API directly, 
# by sending a POST request with JSON data to the web site.
# It returns JSON data, displayed in the console.

import requests
import json

# test 1 = write a title and body here, and send it
a_title = 'How do I call the default deserializer from a custom deserializer in Jackson'

a_body = " <p>I have a problem in my custom deserializer in Jackson. I want to access the default serializer to populate the object I am deserializing into. After the population I will do some custom things but first I want to deserialize the object with the default Jackson behavior.</p>\n\n<p>This is the code that I have at the moment.</p>\n\n<pre><code>public class UserEventDeserializer extends StdDeserializer&lt;User&gt; {\n\n private static final long serialVersionUID = 7923585097068641765L;\n\n public UserEventDeserializer() {\n super(User.class);\n }\n\n @Override\n @Transactional\n public User deserialize(JsonParser jp, DeserializationContext ctxt)\n throws IOException, JsonProcessingException {\n\n ObjectCodec oc = jp.getCodec();\n JsonNode node = oc.readTree(jp);\n User deserializedUser = null;\n deserializedUser = super.deserialize(jp, ctxt, new User()); \n // The previous line generates an exception java.lang.UnsupportedOperationException\n // Because there is no implementation of the deserializer.\n // I want a way to access the default spring deserializer for my User class.\n // How can I do that?\n\n //Special logic\n\n return deserializedUser;\n }\n\n}\n</code></pre>\n\n<p>What I need is a way to initialize the default deserializer so that I can pre-populate my POJO before I start my special logic.</p>\n\n<p>When calling deserialize from within the custom deserializer It seems the method is called from the current context no matter how I construct the serializer class. Because of the annotation in my POJO. This causes a Stack Overflow exception for obvious reasons.</p>\n\n<p>I have tried initializing a <code>BeanDeserializer</code> but the process is extremely complex and I haven't managed to find the right way to do it. I have also tried overloading the <code>AnnotationIntrospector</code> to no avail, thinking that it might help me ignore the annotation in the <code>DeserializerContext</code>. Finally it seams I might have had some success using <code>JsonDeserializerBuilders</code> although this required me to do some magic stuff to get hold of the application context from Spring. I would appreciate any thing that could lead me to a cleaner solution for example how Can I construct a deserialization context without reading the <code>JsonDeserializer</code> annotation.</p>\n"

url = "https://tags-api.herokuapp.com/api/"
#url = "http://127.0.0.1:5000/api/"
headers = {'Content-type': 'application/json'}

dict = {'title': a_title, 'body': a_body}

print('\nA post request has been sent to the API ({}) :\n{}'.format(url, dict))
response = requests.post(url, json=dict, headers=headers)

if response.status_code != 200:
    print('error : ', response)
else:
    print('\nHere is the answer:')
    print(response.text)