from django.db import models

class VMTemplate(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    os = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    cpu = models.IntegerField()
    ram = models.IntegerField()
    disk = models.IntegerField()

    def __str__(self):
        return self.name

    def as_dict(self):
        return {
                "name": self.name,
                "os": self.os,
                "description": self.description,
                "cpu": self.cpu,
                "ram": self.ram,
                "disk": self.disk
                }


class Area(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    subnet = models.CharField(max_length=100)
    next_ip = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def as_dict(self):
        return {
                "name": self.name,
                "subnet": self.subnet,
                "next_ip": self.next_ip
                }


class Workspace(models.Model):
    name = models.CharField(max_length=30, primary_key=True)

    def __str__(self):
        return self.name

    def as_dict(self):
        return {
            "name": self.name
        }


class Network(models.Model):
    class Meta:
        unique_together = (('name', 'owner'))

    states = (('U', 'Up'), ('C', 'Creating'))
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(Workspace, related_name='n_workspace', on_delete=models.CASCADE)
    description = models.CharField(max_length=300, blank=True)
    state = models.CharField(max_length=20, choices=states, default='C')

    def __str__(self):
        return self.name

    def as_dict(self):
        return {
                "name": self.name,
                "owner": self.owner.name,
                "description": self.description,
                "state": self.state
                }


class VM(models.Model):
    class Meta:
        unique_together = (('name', 'owner'))

    states = (('C_D', 'Creating_Disk'), ('C_N', 'Configuring_Network'), ('U',
        'UP'), ('D', 'Down'))
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(Workspace, related_name='vm_workspace', on_delete=models.CASCADE)
    description = models.CharField(max_length=300, blank=True)
    ip = models.CharField(max_length=200)
    state = models.CharField(max_length=20, choices=states, default='C_D')
    area = models.ForeignKey(Area, related_name='area', on_delete=models.CASCADE)
    template = models.ForeignKey(VMTemplate, related_name='template', on_delete=models.CASCADE)
    networks = models.ManyToManyField("Network")

    def __str__(self):
        return self.name

    def as_dict(self):
        return {
                "name": self.name,
                "owner": self.owner.name,
                "description": self.description,
                "ip": self.ip,
                "state": self.state,
                "area": self.area.name,
                "template": self.template.name,
                "networks": [{'name': network.name for network in self.networks.all()}]
                }


class FreeIP(models.Model):
    ip = models.CharField(max_length=200)
    area = models.ForeignKey(Area, related_name='f_area', on_delete=models.CASCADE)

    def __str__(self):
        return self.ip

    def as_dict(self):
        return {
                "ip": self.ip,
                "area": self.area
                }



class Router(models.Model):
    class Meta:
        unique_together = (('name', 'owner'))
    
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(Workspace, related_name='r_workspace', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def as_dict(self):
        return {
            "name": self.name,
            "owner": self.owner.name,
            "interfaces": [{"network": iface.network.name} for iface in RouterInterface.objects.all().filter(router=self)]
        }



class RouterInterface(models.Model):
    class Meta:
        unique_together = (('network', 'router'))

    ip = models.CharField(max_length=200)
    network = models.ForeignKey(Network, related_name='iface', on_delete=models.CASCADE)
    router = models.ForeignKey(Router, related_name='router', on_delete=models.CASCADE)

    def __str__(self):
        return self.network.name

    def as_dict(self):
        return {
            "ip": self.ip,
            "network": self.network.name
        }