from django.db import models

class Scholarship(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    allowance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    slots = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Applicant(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthdate = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    contact_no = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Application(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    scholarship = models.ForeignKey(Scholarship, on_delete=models.CASCADE)
    date_applied = models.DateTimeField(blank=True, null=True)

    status = models.CharField(max_length=50, default="Pending")
    remarks = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Application #{self.id} - {self.applicant}"


class Document(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    doc_type = models.CharField(max_length=100)
    file_path = models.CharField(max_length=500)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.doc_type} - {self.applicant}"


class Evaluation(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    evaluator = models.CharField(max_length=150)
    score = models.FloatField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    eval_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Evaluation for Application #{self.application.id}"


class Beneficiary(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    scholarship = models.ForeignKey(Scholarship, on_delete=models.CASCADE)
    awarded_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=50, default="Active")
    notes = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Beneficiaries"

    def __str__(self):
        return f"Beneficiary: {self.applicant} - {self.scholarship}"