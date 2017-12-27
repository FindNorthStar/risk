# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Abnormaltaxinfo(models.Model):
    platform_name = models.CharField(max_length=45, blank=True, null=True)
    notice_date = models.DateField(blank=True, null=True)
    data_type = models.CharField(max_length=45, blank=True, null=True)
    identity_id = models.CharField(max_length=450, blank=True, null=True)
    company_name = models.CharField(max_length=250, blank=True, null=True)
    notice_title = models.CharField(max_length=450, blank=True, null=True)
    notice_type = models.CharField(max_length=45, blank=True, null=True)
    notice_department = models.CharField(max_length=450, blank=True, null=True)
    title = models.CharField(max_length=450, blank=True, null=True)
    tax_num = models.CharField(max_length=45, blank=True, null=True)
    legal_person = models.CharField(max_length=45, blank=True, null=True)
    notice_time = models.CharField(max_length=45, blank=True, null=True)
    abnormal_tax_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'abnormalTaxInfo'


class Administrationpenalty(models.Model):
    platform_name = models.CharField(max_length=45, blank=True, null=True)
    incident_time = models.CharField(max_length=45, blank=True, null=True)
    person_name = models.CharField(max_length=450, blank=True, null=True)
    case_type = models.CharField(max_length=4500, blank=True, null=True)
    case_num = models.CharField(max_length=45, blank=True, null=True)
    illegal_type = models.CharField(max_length=45, blank=True, null=True)
    excute_type = models.CharField(max_length=45, blank=True, null=True)
    case_result = models.CharField(max_length=45, blank=True, null=True)
    penalty_decide_document = models.CharField(max_length=450, blank=True, null=True)
    penalty_decide_date = models.CharField(max_length=45, blank=True, null=True)
    penalty_decide_department = models.CharField(max_length=450, blank=True, null=True)
    main_illegal_content = models.CharField(max_length=4500, blank=True, null=True)
    penalty_reason = models.CharField(max_length=4500, blank=True, null=True)
    penalty_type = models.CharField(max_length=45, blank=True, null=True)
    penalty_result = models.CharField(max_length=45, blank=True, null=True)
    penalty_amount = models.CharField(max_length=45, blank=True, null=True)
    penalty_execute_result = models.CharField(max_length=450, blank=True, null=True)
    administration_penalty_content = models.CharField(max_length=450, blank=True, null=True)
    penalty_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'administrationPenalty'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_groups'


class AuthUserUserPermissions(models.Model):
    user_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'


class Bankdepository(models.Model):
    platform_name = models.CharField(max_length=45, blank=True, null=True)
    company_name = models.CharField(max_length=450, blank=True, null=True)
    website_url = models.CharField(max_length=450, blank=True, null=True)
    is_bank_depository = models.CharField(max_length=45, blank=True, null=True)
    is_depository = models.CharField(max_length=45, blank=True, null=True)
    platform_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'bankDepository'


class Branchinfo(models.Model):
    platform_name = models.CharField(max_length=45, blank=True, null=True)
    branch_name = models.CharField(max_length=450, blank=True, null=True)
    branch_register_num = models.CharField(max_length=45, blank=True, null=True)
    register_code = models.CharField(max_length=45, blank=True, null=True)
    branch_charge_person = models.CharField(max_length=45, blank=True, null=True)
    common_bussiness_project = models.CharField(max_length=450, blank=True, null=True)
    branch_address = models.CharField(max_length=450, blank=True, null=True)
    branch_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'branchInfo'


class Businessinfo(models.Model):
    platform_name = models.CharField(max_length=45, blank=True, null=True)
    end_time = models.DateField(blank=True, null=True)
    trade_amount = models.FloatField(blank=True, null=True)
    trade_total_number = models.FloatField(blank=True, null=True)
    invest_total_number = models.FloatField(blank=True, null=True)
    financiers_number = models.FloatField(blank=True, null=True)
    invester_number = models.FloatField(blank=True, null=True)
    repaid_amount = models.FloatField(blank=True, null=True)
    past_amount = models.FloatField(blank=True, null=True)
    project_past_rate = models.FloatField(blank=True, null=True)
    amount_past_rate = models.FloatField(blank=True, null=True)
    project_past_number = models.FloatField(blank=True, null=True)
    average_financialer_amount = models.FloatField(blank=True, null=True)
    average_invest_amount = models.FloatField(blank=True, null=True)
    average_finacing_amount = models.FloatField(blank=True, null=True)
    top1_finacing_rate = models.FloatField(blank=True, null=True)
    top10_finacing_rate = models.FloatField(blank=True, null=True)
    top1_invest_rate = models.FloatField(blank=True, null=True)
    top10_invest_rate = models.FloatField(blank=True, null=True)
    project_past90_rate = models.FloatField(blank=True, null=True)
    project_past180_rate = models.FloatField(blank=True, null=True)
    project_past181_rate = models.FloatField(blank=True, null=True)
    amount_past90_rate = models.FloatField(blank=True, null=True)
    amount_past180_rate = models.FloatField(blank=True, null=True)
    amount_past181_rate = models.FloatField(blank=True, null=True)
    history_project_past_amount = models.FloatField(blank=True, null=True)
    history_project_past_rate = models.FloatField(blank=True, null=True)
    total_past_amount = models.FloatField(blank=True, null=True)
    total_past_number = models.FloatField(blank=True, null=True)
    bussinessinfoid = models.AutoField(db_column='bussinessInfoId', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'businessInfo'


class Businessinvestinfo(models.Model):
    platform_name = models.CharField(max_length=45, blank=True, null=True)
    company_name = models.CharField(max_length=250, blank=True, null=True)
    register_num = models.BigIntegerField(blank=True, null=True)
    credit_code = models.CharField(max_length=45, blank=True, null=True)
    business_type = models.CharField(max_length=450, blank=True, null=True)
    register_capital = models.CharField(max_length=45, blank=True, null=True)
    register_currency = models.CharField(max_length=45, blank=True, null=True)
    end_date = models.CharField(max_length=45, blank=True, null=True)
    revoke_date = models.CharField(max_length=45, blank=True, null=True)
    business_state = models.CharField(max_length=45, blank=True, null=True)
    register_department = models.CharField(max_length=450, blank=True, null=True)
    invest_amount = models.CharField(max_length=45, blank=True, null=True)
    invest_currency = models.CharField(max_length=45, blank=True, null=True)
    invest_percent = models.CharField(max_length=45, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    legal_preson = models.CharField(max_length=45, blank=True, null=True)
    invest_type = models.CharField(max_length=45, blank=True, null=True)
    invest_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'businessInvestInfo'


class Changeinfo(models.Model):
    platform_name = models.CharField(max_length=45, blank=True, null=True)
    change_date = models.DateField(blank=True, null=True)
    change_project = models.CharField(max_length=450, blank=True, null=True)
    change_before_content = models.CharField(max_length=4500, blank=True, null=True)
    change_after_content = models.CharField(max_length=4500, blank=True, null=True)
    change_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'changeInfo'


class Changesummary(models.Model):
    platform = models.CharField(max_length=450, blank=True, null=True)
    company = models.CharField(max_length=450, blank=True, null=True)
    manager_change = models.IntegerField(blank=True, null=True)
    stock_change = models.IntegerField(blank=True, null=True)
    register_change = models.IntegerField(blank=True, null=True)
    max_register_change = models.IntegerField(blank=True, null=True)
    other_change = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'changeSummary'


class Company(models.Model):
    platform_name = models.CharField(max_length=45, blank=True, null=True)
    legal_person = models.CharField(max_length=90, blank=True, null=True)
    register_num = models.BigIntegerField(blank=True, null=True)
    company_name = models.CharField(unique=True, max_length=250, blank=True, null=True)
    credit_code = models.CharField(max_length=45, blank=True, null=True)
    register_before = models.CharField(max_length=45, blank=True, null=True)
    register_capital = models.FloatField(blank=True, null=True)
    currency = models.CharField(max_length=45, blank=True, null=True)
    paid_in_capital = models.CharField(max_length=450, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    business_start_date = models.DateField(blank=True, null=True)
    business_end_date = models.CharField(max_length=45, blank=True, null=True)
    company_type = models.CharField(max_length=450, blank=True, null=True)
    business_state = models.CharField(max_length=45, blank=True, null=True)
    end_date = models.CharField(max_length=45, blank=True, null=True)
    revoke_date = models.CharField(max_length=45, blank=True, null=True)
    address = models.CharField(max_length=450, blank=True, null=True)
    permit_business = models.CharField(max_length=4500, blank=True, null=True)
    general_business = models.CharField(max_length=4500, blank=True, null=True)
    business_scope = models.CharField(max_length=4500, blank=True, null=True)
    business_pattern = models.CharField(max_length=4500, blank=True, null=True)
    register_department = models.CharField(max_length=450, blank=True, null=True)
    telephone = models.CharField(max_length=90, blank=True, null=True)
    check_day = models.CharField(max_length=45, blank=True, null=True)
    last_check_year = models.CharField(max_length=45, blank=True, null=True)
    last_check_day = models.CharField(max_length=45, blank=True, null=True)
    trade_type_code = models.CharField(max_length=45, blank=True, null=True)
    trade_type_code_old = models.CharField(max_length=45, blank=True, null=True)
    trade_type = models.CharField(max_length=450, blank=True, null=True)
    economy_code = models.CharField(max_length=90, blank=True, null=True)
    economt_name = models.CharField(max_length=90, blank=True, null=True)
    change_date = models.CharField(max_length=90, blank=True, null=True)
    company_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'company'


class CompanyList(models.Model):
    platform = models.CharField(max_length=450, blank=True, null=True)
    company = models.CharField(max_length=450, blank=True, null=True)
    area_code = models.CharField(max_length=10, blank=True, null=True)
    area = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company_list'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Documentexecute(models.Model):
    platform_name = models.CharField(max_length=45, blank=True, null=True)
    case_date = models.DateField(blank=True, null=True)
    execute_department = models.CharField(max_length=45, blank=True, null=True)
    identify_code = models.CharField(max_length=100, blank=True, null=True)
    case_id = models.CharField(db_column='case_Id', max_length=100, blank=True, null=True)  # Field name made lowercase.
    date_type = models.CharField(max_length=15, blank=True, null=True)
    executed_name = models.CharField(max_length=100, blank=True, null=True)
    case_no = models.CharField(max_length=45, blank=True, null=True)
    case_status = models.CharField(max_length=45, blank=True, null=True)
    target = models.CharField(max_length=20, blank=True, null=True)
    content = models.CharField(max_length=500, blank=True, null=True)
    city = models.CharField(max_length=45, blank=True, null=True)
    title = models.CharField(max_length=45, blank=True, null=True)
    province = models.CharField(max_length=45, blank=True, null=True)
    release_time = models.CharField(max_length=45, blank=True, null=True)
    document_executidl = models.AutoField(db_column='document_executIdl', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'documentExecute'


class Documentjudgment(models.Model):
    platform_name = models.CharField(max_length=45, blank=True, null=True)
    used_name = models.CharField(max_length=45, blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    document_type = models.CharField(max_length=45, blank=True, null=True)
    data_type = models.CharField(max_length=45, blank=True, null=True)
    title = models.CharField(max_length=450, blank=True, null=True)
    judgementid = models.CharField(db_column='judgementId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    court_name = models.CharField(max_length=200, blank=True, null=True)
    case_no = models.CharField(max_length=100, blank=True, null=True)
    case_type = models.CharField(max_length=45, blank=True, null=True)
    judge_money = models.CharField(max_length=450, blank=True, null=True)
    judg_name = models.CharField(max_length=450, blank=True, null=True)
    city = models.CharField(max_length=45, blank=True, null=True)
    case_brief = models.CharField(max_length=100, blank=True, null=True)
    juryman = models.CharField(max_length=450, blank=True, null=True)
    province = models.CharField(max_length=45, blank=True, null=True)
    judge_result1 = models.CharField(max_length=45, blank=True, null=True)
    judge_result2 = models.CharField(max_length=3000, blank=True, null=True)
    accordings = models.CharField(max_length=450, blank=True, null=True)
    departmentno = models.CharField(max_length=45, blank=True, null=True)
    event_date = models.CharField(max_length=45, blank=True, null=True)
    process = models.CharField(max_length=25, blank=True, null=True)
    third_person = models.CharField(max_length=450, blank=True, null=True)
    clerker = models.CharField(max_length=45, blank=True, null=True)
    accuser = models.CharField(max_length=2000, blank=True, null=True)
    document_judgmentid = models.AutoField(db_column='document_judgmentId', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'documentJudgment'


class Employinfo(models.Model):
    platform_name = models.CharField(max_length=45, blank=True, null=True)
    sorttime = models.CharField(db_column='sortTime', max_length=45, blank=True, null=True)  # Field name made lowercase.
    datatype = models.CharField(db_column='dataType', max_length=45, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(max_length=200, blank=True, null=True)
    startdate = models.CharField(db_column='startDate', max_length=45, blank=True, null=True)  # Field name made lowercase.
    stopdate = models.CharField(db_column='stopDate', max_length=45, blank=True, null=True)  # Field name made lowercase.
    property = models.CharField(max_length=45, blank=True, null=True)
    province = models.CharField(max_length=45, blank=True, null=True)
    salary = models.CharField(max_length=100, blank=True, null=True)
    departmentid = models.CharField(db_column='departmentId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    average_salary = models.CharField(max_length=45, blank=True, null=True)
    welfare = models.CharField(max_length=100, blank=True, null=True)
    avg_work_experience = models.CharField(max_length=100, blank=True, null=True)
    trade = models.CharField(max_length=100, blank=True, null=True)
    work_experience = models.CharField(max_length=100, blank=True, null=True)
    education = models.CharField(max_length=45, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    employer_num = models.CharField(max_length=45, blank=True, null=True)
    employinfoid = models.AutoField(db_column='employInfoId', primary_key=True)  # Field name made lowercase.
    startmonth = models.CharField(db_column='startMonth', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'employInfo'


class Equitypledged(models.Model):
    platform_name = models.CharField(max_length=45, blank=True, null=True)
    equitypledged_person = models.CharField(max_length=45, blank=True, null=True)
    equitypledged_type = models.CharField(max_length=45, blank=True, null=True)
    equitypledged_money = models.FloatField(blank=True, null=True)
    equitypledged_record_date = models.CharField(max_length=45, blank=True, null=True)
    equitypledged_approve_department = models.CharField(max_length=45, blank=True, null=True)
    equitypledged_approve_date = models.CharField(max_length=45, blank=True, null=True)
    equitypledged_end_date = models.CharField(max_length=45, blank=True, null=True)
    equitypledgedid = models.AutoField(db_column='equitypledgedId', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'equityPledged'


class Failcredit(models.Model):
    company_name = models.CharField(max_length=450, blank=True, null=True)
    credit_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'failCredit'


class Freezeinfo(models.Model):
    platform_name = models.CharField(max_length=45, blank=True, null=True)
    freeze_reference_no = models.CharField(max_length=450, blank=True, null=True)
    freeze_department = models.CharField(max_length=100, blank=True, null=True)
    freeze_start_date = models.CharField(max_length=100, blank=True, null=True)
    freeze_end_date = models.CharField(max_length=100, blank=True, null=True)
    freeze_money = models.CharField(max_length=100, blank=True, null=True)
    unfreeze_department = models.CharField(max_length=45, blank=True, null=True)
    unfreeze_number = models.CharField(max_length=100, blank=True, null=True)
    unfreeze_date = models.CharField(max_length=100, blank=True, null=True)
    unfreeze_description = models.CharField(max_length=450, blank=True, null=True)
    freezeid = models.AutoField(db_column='freezeId', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'freezeInfo'


class Guotai(models.Model):
    fullname = models.CharField(db_column='FullName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    tradingdate = models.DateField(db_column='TradingDate', blank=True, null=True)  # Field name made lowercase.
    tradingvolume = models.FloatField(db_column='TradingVolume', blank=True, null=True)  # Field name made lowercase.
    avereturn = models.FloatField(db_column='AveReturn', blank=True, null=True)  # Field name made lowercase.
    investornum = models.IntegerField(db_column='InvestorNum', blank=True, null=True)  # Field name made lowercase.
    avelimtime = models.FloatField(db_column='AveLimTime', blank=True, null=True)  # Field name made lowercase.
    loannum = models.IntegerField(db_column='LoanNum', blank=True, null=True)  # Field name made lowercase.
    cumulaterepay = models.FloatField(db_column='CumulateRepay', blank=True, null=True)  # Field name made lowercase.
    f30repay = models.FloatField(db_column='F30Repay', blank=True, null=True)  # Field name made lowercase.
    f60repay = models.FloatField(db_column='F60Repay', blank=True, null=True)  # Field name made lowercase.
    guotaiid = models.AutoField(db_column='guotaiId', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'guotai'


class Icp(models.Model):
    company_name = models.CharField(max_length=250, blank=True, null=True)
    company_type = models.CharField(max_length=45, blank=True, null=True)
    licence_num = models.CharField(max_length=45, blank=True, null=True)
    website_name = models.CharField(max_length=450, blank=True, null=True)
    website_url = models.CharField(max_length=450, blank=True, null=True)
    examine_date = models.DateField(blank=True, null=True)
    is_restriction = models.CharField(max_length=45, blank=True, null=True)
    icpcol = models.CharField(max_length=45, blank=True, null=True)
    company_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'icp'


class Legalpersoninvestinfo(models.Model):
    platform_name = models.CharField(max_length=45, blank=True, null=True)
    company_name = models.CharField(max_length=250, blank=True, null=True)
    register_num = models.CharField(max_length=45, blank=True, null=True)
    credit_code = models.CharField(max_length=45, blank=True, null=True)
    business_type = models.CharField(max_length=45, blank=True, null=True)
    register_capital = models.CharField(max_length=45, blank=True, null=True)
    currency = models.CharField(max_length=45, blank=True, null=True)
    end_date = models.CharField(max_length=45, blank=True, null=True)
    revoke_date = models.CharField(max_length=45, blank=True, null=True)
    business_state = models.CharField(max_length=45, blank=True, null=True)
    register_department = models.CharField(max_length=450, blank=True, null=True)
    invest_amount = models.CharField(max_length=45, blank=True, null=True)
    invest_currency = models.CharField(max_length=45, blank=True, null=True)
    invest_percent = models.CharField(max_length=45, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    legal_preson = models.CharField(max_length=45, blank=True, null=True)
    invest_type = models.CharField(max_length=45, blank=True, null=True)
    invest_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'legalPersonInvestInfo'


class Legalpersonpositioninfo(models.Model):
    platform_name = models.CharField(max_length=45, blank=True, null=True)
    legal_person_name = models.CharField(max_length=450, blank=True, null=True)
    company_name = models.CharField(max_length=250, blank=True, null=True)
    credit_code = models.CharField(max_length=45, blank=True, null=True)
    register_num = models.CharField(max_length=45, blank=True, null=True)
    business_type = models.CharField(max_length=45, blank=True, null=True)
    register_capital = models.CharField(max_length=45, blank=True, null=True)
    register_currency = models.CharField(max_length=45, blank=True, null=True)
    business_state = models.CharField(max_length=45, blank=True, null=True)
    end_date = models.CharField(max_length=45, blank=True, null=True)
    revoke_date = models.CharField(max_length=45, blank=True, null=True)
    register_department = models.CharField(max_length=45, blank=True, null=True)
    position = models.CharField(max_length=45, blank=True, null=True)
    is_legal_person = models.CharField(max_length=45, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    person_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'legalPersonPositionInfo'


class Liquidation(models.Model):
    platform_name = models.CharField(max_length=45, blank=True, null=True)
    liquidation_person_liable = models.CharField(max_length=45, blank=True, null=True)
    liquidation_responsible_person = models.CharField(max_length=45, blank=True, null=True)
    liquidation_responsible_person_2 = models.CharField(max_length=45, blank=True, null=True)
    liquidation_completed_situation = models.CharField(max_length=450, blank=True, null=True)
    liquidation_completed_date = models.CharField(max_length=45, blank=True, null=True)
    debt_holder = models.CharField(max_length=45, blank=True, null=True)
    creditor_receiver = models.CharField(max_length=45, blank=True, null=True)
    liquidationid = models.AutoField(db_column='liquidationId', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'liquidation'


class Managerinfo(models.Model):
    platform_name = models.CharField(max_length=45, blank=True, null=True)
    manager_name = models.CharField(max_length=450, blank=True, null=True)
    position = models.CharField(max_length=45, blank=True, null=True)
    gender = models.CharField(max_length=45, blank=True, null=True)
    manager_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'managerInfo'


class News(models.Model):
    platform_name = models.CharField(max_length=45, blank=True, null=True)
    news_time = models.DateField(blank=True, null=True)
    data_type = models.CharField(max_length=45, blank=True, null=True)
    news_title = models.CharField(max_length=10000, blank=True, null=True)
    label = models.CharField(max_length=10000, blank=True, null=True)
    keywords = models.CharField(max_length=1000, blank=True, null=True)
    news_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'news'


class Platform(models.Model):
    name = models.CharField(unique=True, max_length=45, blank=True, null=True)
    region = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'platform'


class Shareholderinfo(models.Model):
    platform_name = models.CharField(max_length=45, blank=True, null=True)
    shareholder_name = models.CharField(max_length=450, blank=True, null=True)
    share_amount = models.CharField(max_length=45, blank=True, null=True)
    currency = models.CharField(max_length=45, blank=True, null=True)
    invest_date = models.CharField(max_length=45, blank=True, null=True)
    register_date = models.CharField(max_length=45, blank=True, null=True)
    share_percent = models.CharField(max_length=45, blank=True, null=True)
    nation = models.CharField(max_length=45, blank=True, null=True)
    shareholder_type = models.CharField(max_length=45, blank=True, null=True)
    invest_type = models.CharField(max_length=45, blank=True, null=True)
    invest_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'shareholderInfo'


class Taxcreditinfo(models.Model):
    platform_name = models.CharField(max_length=45, blank=True, null=True)
    evaluate_year = models.CharField(max_length=45, blank=True, null=True)
    data_type = models.CharField(max_length=45, blank=True, null=True)
    company_name = models.CharField(max_length=250, blank=True, null=True)
    notice_title = models.CharField(max_length=450, blank=True, null=True)
    notice_type = models.CharField(max_length=45, blank=True, null=True)
    notice_department = models.CharField(max_length=450, blank=True, null=True)
    title = models.CharField(max_length=450, blank=True, null=True)
    tax_payer_id = models.CharField(max_length=45, blank=True, null=True)
    credit_level = models.CharField(max_length=45, blank=True, null=True)
    notice_time = models.CharField(max_length=45, blank=True, null=True)
    credit_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'taxCreditInfo'


class Taxinfo(models.Model):
    platform_name = models.CharField(max_length=45, blank=True, null=True)
    owe_tax_date = models.DateField(blank=True, null=True)
    data_type = models.CharField(max_length=45, blank=True, null=True)
    company_name = models.CharField(max_length=250, blank=True, null=True)
    notice_title = models.CharField(max_length=450, blank=True, null=True)
    notice_content = models.CharField(max_length=4500, blank=True, null=True)
    notice_type = models.CharField(max_length=45, blank=True, null=True)
    tax_type = models.CharField(max_length=450, blank=True, null=True)
    notice_department = models.CharField(max_length=450, blank=True, null=True)
    title = models.CharField(max_length=450, blank=True, null=True)
    public_time = models.CharField(max_length=45, blank=True, null=True)
    tax_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'taxInfo'


class Taxpenalty(models.Model):
    platform_name = models.CharField(max_length=45, blank=True, null=True)
    penalty_date = models.DateField(blank=True, null=True)
    data_type = models.CharField(max_length=45, blank=True, null=True)
    company_name = models.CharField(max_length=250, blank=True, null=True)
    notice_title = models.CharField(max_length=450, blank=True, null=True)
    notice_type = models.CharField(max_length=45, blank=True, null=True)
    notice_department = models.CharField(max_length=450, blank=True, null=True)
    title = models.CharField(max_length=450, blank=True, null=True)
    legal_person = models.CharField(max_length=45, blank=True, null=True)
    notice_date = models.CharField(max_length=45, blank=True, null=True)
    penalty_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'taxPenalty'


class Wdzjinfo(models.Model):
    wdzjinfoid = models.AutoField(db_column='wdzjInfoId', primary_key=True)  # Field name made lowercase.
    platform_name = models.CharField(max_length=45, blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    incomerate = models.FloatField(db_column='incomeRate', blank=True, null=True)  # Field name made lowercase.
    loanperiod = models.FloatField(db_column='loanPeriod', blank=True, null=True)  # Field name made lowercase.
    regcapital = models.FloatField(db_column='regCapital', blank=True, null=True)  # Field name made lowercase.
    fullloantime = models.FloatField(db_column='fullloanTime', blank=True, null=True)  # Field name made lowercase.
    staystilloftotal = models.FloatField(db_column='stayStillOfTotal', blank=True, null=True)  # Field name made lowercase.
    netinflowofthirty = models.FloatField(db_column='netInflowOfThirty', blank=True, null=True)  # Field name made lowercase.
    timeoperation = models.FloatField(db_column='timeOperation', blank=True, null=True)  # Field name made lowercase.
    biddernum = models.FloatField(db_column='bidderNum', blank=True, null=True)  # Field name made lowercase.
    borrowernum = models.FloatField(db_column='borrowerNum', blank=True, null=True)  # Field name made lowercase.
    totalloannum = models.FloatField(db_column='totalLoanNum', blank=True, null=True)  # Field name made lowercase.
    top10dueinproportion = models.FloatField(db_column='top10DueInProportion', blank=True, null=True)  # Field name made lowercase.
    avgbidmoney = models.FloatField(db_column='avgBidMoney', blank=True, null=True)  # Field name made lowercase.
    top10staystillproportion = models.FloatField(db_column='top10StayStillProportion', blank=True, null=True)  # Field name made lowercase.
    avgborrowmoney = models.FloatField(db_column='avgBorrowMoney', blank=True, null=True)  # Field name made lowercase.
    developzhishu = models.FloatField(db_column='developZhishu', blank=True, null=True)  # Field name made lowercase.
    currentleverageamount = models.FloatField(db_column='currentLeverageAmount', blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateField(db_column='startDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateField(db_column='endDate', blank=True, null=True)  # Field name made lowercase.
    weightedamount = models.FloatField(db_column='weightedAmount', blank=True, null=True)  # Field name made lowercase.
    background = models.CharField(max_length=45, blank=True, null=True)
    newbackground = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wdzjInfo'
