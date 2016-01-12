from django.db import models


class BuildJob(models.Model):
    id = models.CharField(primary_key=True, max_length=100)

    name = models.CharField(max_length=256)
    url = models.URLField()

    manifest = models.TextField(blank=True)
    branch_name = models.CharField(blank=True, max_length=256)

    gerrit_change_id = models.CharField(blank=True, max_length=256)
    gerrit_change_number = models.CharField(blank=True, max_length=256)
    gerrit_patchset_number = models.CharField(blank=True, max_length=256)
    gerrit_change_url = models.URLField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return '%s %s' % (self.id, self.name)


class TestJob(models.Model):
    build_job = models.ForeignKey('BuildJob', related_name="test_jobs")

    id = models.CharField(primary_key=True, max_length=100)

    url = models.URLField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    status = models.CharField(blank=True, null=True, max_length=16)
    created_at = models.DateTimeField(auto_now_add=True)
    definition = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return '%s %s' % (self.id, self.build_job)


