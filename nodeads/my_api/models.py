from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=64, blank=False, null=False)
    dscr = models.CharField(max_length=128, blank=True, null=True)
    image = models.ImageField(blank=False, null=False)
    num_child_groups = models.IntegerField(blank=True, null=True, default=0)
    num_child_elements = models.IntegerField(blank=True, null=True, default=0)
    parent_group = models.ForeignKey('Group', null=True, blank=True, on_delete=models.CASCADE)

    def update_num_of_children(self, *args, **kwargs):
        self.num_child_groups = Group.objects.filter(parent_group=self).count()
        self.num_child_elements = Element.objects.filter(parent_group=self).filter(checked__isnull=False).count()
        super().save(*args, **kwargs)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.parent_group is not None:
            self.parent_group.update_num_of_children()

    def __str__(self):
        return 'id: {}, name: {}'.format(self.id, self.name)

class Element(models.Model):
    name = models.CharField(max_length=64, blank=False, null=False)
    dscr = models.CharField(max_length=128, blank=True, null=True)
    image = models.ImageField(blank=False, null=False)
    checked = models.BooleanField(default=None,null=True, blank=True)
    date_of_creation = models.DateField(auto_now_add=True)
    parent_group = models.ForeignKey('Group', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.parent_group is not None:
            self.parent_group.update_num_of_children()


    def __str__(self):
        return '{}, id: {}, name: {}'.format('Null' if self.checked is None else self.checked, self.id, self.name)
