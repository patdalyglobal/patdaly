from django.db import models
from django.utils import formats
from django.dispatch import receiver
from django.db.models.signals import pre_save
# Create your models here.

class ContactMessage(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.subject}"

    class Meta:
        ordering = ['-created_at']


#-------------------------- For Plateau State Ministry of Budget and Planning-------------#
# models.py

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Contractor(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone_number = models.CharField(max_length=15, help_text='Enter phone number in the format +2348012345678', unique=True, verbose_name='Phone Number')
    rc_number = models.CharField(max_length=20, help_text='Enter RC Number in the format BN12345', unique=True, verbose_name='RC Number')

    def __str__(self):
        return self.name

class Supervisor(models.Model):
    name = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    id_number = models.CharField(max_length=20, unique=True, verbose_name='ID Number')

    def __str__(self):
        return self.name


class Project(models.Model):
    status_option = (
        ('', 'Select Option'),
        ('1', 'Yes'),
        ('2', 'No'),
    )
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=20, unique=True, verbose_name='Code', editable=False)
    location = models.CharField(max_length=255)
    date_awarded = models.DateField(verbose_name='Date Awarded', null=True, blank=True, default=True)
    date_contract_reviewed = models.DateField(verbose_name='Date Contract Reviewed', null=True, blank=True)
    contract_sum = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Contract Sum (in Naira)')
    revised_contract_sum = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Revised Contract Sum', null=True, blank=True)
    completion_status = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        verbose_name='Completion Status (%)'
    )
    project_completed = models.CharField(max_length=4, choices=status_option)
    contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE, verbose_name='Contractor')
    supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE, verbose_name='Supervised by')

    def __str__(self):
        return self.name

    def formatted_contract_sum(self):
        return formats.number_format(self.contract_sum, use_l10n=True)

    def formatted_revised_contract_sum(self):
        return formats.number_format(self.revised_contract_sum, use_l10n=True)


# Define the function outside the class
def generate_code(location):
    location_codes = {
        'mg': 'Mangu',
        'ln': 'Langtang-North',
        'js': 'Jos-South',
        'bs': 'Basa'
        # Add more location codes as needed
    }

    code_abbr = location.split('-')[0].lower()

    if code_abbr in location_codes:
        # Fetch the latest project code for the specific location
        latest_project = Project.objects.filter(location__startswith=code_abbr).order_by('-code').first()

        if latest_project:
            # Extract the last part of the code (e.g., 'pl-mg-001-002' -> '002')
            last_part = latest_project.code.split('-')[-1]
            last_number = int(last_part) + 1
            new_code = f'{last_number:03d}'
        else:
            new_code = '001'

        return f'pl-{code_abbr}-{new_code}-{new_code}'

    return ''


# Use a signal outside the class to generate the code before saving
@receiver(pre_save, sender=Project)
def generate_project_code(sender, instance, **kwargs):
    if not instance.code:
        instance.code = generate_code(instance.location)