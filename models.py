import datetime
from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
from custom.models import *
from employee.models import *

# Create your models here.

class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)
	

class ContractType(models.Model):
	name = models.CharField(max_length=100)
    
	created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="ContractTypecreatedbys")
	created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="ContractTypeupdatedbys")
	updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
	deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="ContractTypedeletedbys")
	deleted_at = models.DateTimeField(null=True, blank=True)

	def __str__(self):
		template = '{0.name}'
		return template.format(self)

	def delete(self, user):
		self.deleted_at = str(datetime.timezone.now())
		self.deleted_by = user
		self.save()

	default_objects = models.Manager()  # The default manager
	objects = ActiveManager()

	class Meta:
		verbose_name_plural='1-Data-Contract-ContractType'


class Contract(models.Model):
	employeeuser = models.ForeignKey(EmployeeUser, null=True, blank=True, on_delete=models.CASCADE)
	contract_type = models.ForeignKey(ContractType, on_delete=models.CASCADE, null=True, blank=True)
	grade = models.ForeignKey(Grade, on_delete=models.CASCADE, null=True, blank=True)
	position = models.ForeignKey(Position, on_delete=models.CASCADE, null=True)
	nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE, null=True)
	start_date = models.DateField(null=True, blank=True)
	end_date = models.DateField(null=True, blank=True)
	terminate_date = models.DateField(null=True, blank=True)
	reason = models.CharField(max_length=200, null=True, blank=True)
	file = models.FileField(upload_to="upload_contract", null=True, blank=True,
			validators=[FileExtensionValidator(allowed_extensions=['pdf'])], verbose_name="Attach ToR")
	file_end = models.FileField(upload_to="upload_contract_end", null=True, blank=True,
			validators=[FileExtensionValidator(allowed_extensions=['pdf'])], verbose_name="Anekso")
	is_active = models.BooleanField(default=True)
	is_lock = models.BooleanField(default=False, null=True)
    
	created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Contractcreatedbys")
	created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Contractupdatedbys")
	updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
	deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Contractdeletedbys")
	deleted_at = models.DateTimeField(null=True, blank=True)
	
	def __str__(self):
		template = '{0.employeeuser} - {0.position}'
		return template.format(self)

	def delete(self, user):
		self.deleted_at = str(datetime.timezone.now())
		self.deleted_by = user
		self.save()

	default_objects = models.Manager()  # The default manager
	objects = ActiveManager()

	class Meta:
		verbose_name_plural='1-Data-Contract-Contract'

class EmpSalary(models.Model):
	employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, related_name='empsalary')
	contract = models.OneToOneField(Contract, on_delete=models.CASCADE, null=True, blank=True, related_name='empsalary')
	amount = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	is_active = models.BooleanField(default=True, blank=True)
	is_lock = models.BooleanField(default=True, null=True)

	created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="EmpSalarycreatedbys")
	created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="EmpSalaryupdatetedbys")
	updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
	deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="EmpSalarydeletedbys")
	deleted_at = models.DateTimeField(null=True, blank=True)

	def __str__(self):
		template = '{0.contract} - {0.amount}'
		return template.format(self)

	def delete(self, user):
		self.deleted_at = str(timezone.now())
		self.deleted_by = user
		self.save()

	default_objects = models.Manager()  # The default manager
	objects = ActiveManager()
	
	class Meta:
		verbose_name_plural='11-Data-Custom-EmpSalary'


class EmpPlacement(models.Model):
	employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
	position = models.ForeignKey(Position, on_delete=models.CASCADE, null=True, blank=True)	
	department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
	start_date = models.DateField(null=True, blank=True)
	end_date = models.DateField(null=True, blank=True)
	terminate_date = models.DateField(null=True, blank=True)
	reason = models.CharField(max_length=200, null=True, blank=True)
	file = models.FileField(upload_to="upload_place", null=True, blank=True,
			validators=[FileExtensionValidator(allowed_extensions=['pdf'])], verbose_name="Attach Dispatch")
	is_active = models.BooleanField(default=True)
	is_confirm = models.BooleanField(default=False, null=True)
	
	created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="EmpPlacementcreatedbys")
	created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="EmpPlacementupdatetedbys")
	updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
	deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="EmpPlacementdeletedbys")
	deleted_at = models.DateTimeField(null=True, blank=True)

	def __str__(self):
		template = '{0.employee} - {0.de}/{0.unit}/{0.department}'
		return template.format(self)

	def delete(self, user):
		self.deleted_at = str(timezone.now())
		self.deleted_by = user
		self.save()

	default_objects = models.Manager()  # The default manager
	objects = ActiveManager()
	
	class Meta:
		verbose_name_plural='11-Data-Custom-EmpPlacement'