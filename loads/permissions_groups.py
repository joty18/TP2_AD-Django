def run():

    # Create GROUPS and set permissions
    from django.contrib.auth.models import User, Group, Permission

    mygroup, created = Group.objects.get_or_create(name='Utentes')

    permission1 = Permission.objects.get(name='Can view agenda')
    permission2 = Permission.objects.get(name='Can view utente')
    mygroup.permissions.add(permission1, permission2)
    mygroup.save()