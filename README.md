# Django REST API for sending email messages

Rest api build with Django Rest Framework. Api allows to send multiple emails. Main features:
<ul>
<li>sending emails to any addresses (using Celery)</li>
<li>using previously defined messages and topics (Template model)</li>
<li>using previously defined mailbox (Mailbox model)</li>

</ul>

## Used technologies

<ul>
<li>Python</li>
<li>Django, Django Rest Framework (DRF)</li>
<li>django-cookicutter</li>
<li>PostgreSQL</li>
<li>Celery</li>
<li>django-filter</li>
</ul>


### Installing

To install and run this project you must have to installed docker and docker-compose

Building docker images:
```
docker-compose -f local.yml build
```

Run project:

```
docker-compose -f local.yml up
```
### Testing app

To test api you can use tool like Postman

Available api endpoints: TODO
