from django.test import TestCase
from time_tables.models import TimeTable, TimeTableRecord


def create_time_table(study_room=None):
    time_table_name = 'time_table'
    time_table = TimeTable.objects.create(
        study_room=study_room,
        name=time_table_name,
    )
    return time_table


def create_time_table_record(teacher=None, time_table=None, subject=None):
    day_of_week = TimeTableRecord.DayOfWeek.MON
    period = 1
    time_table_record = TimeTableRecord.objects.create(
        teacher=teacher,
        day_of_week=day_of_week,
        period=period,
        time_table=time_table,
        subject=subject,
    )
    return time_table_record


def create_time_tables(new_time_tables_count, study_room=None):
    time_tables = []
    for i in range(new_time_tables_count):
        time_table_name = 'time_table' + str(i+1)
        time_table = TimeTable(
            study_room=study_room,
            name=time_table_name,
        )
        time_tables.append(time_table)
    TimeTable.objects.bulk_create(time_tables)


def create_time_table_records(
        time_table_record_count, day_of_week=TimeTableRecord.DayOfWeek.MON,
        teacher=None, time_table=None, subject=None):
    time_table_records = []
    for period in range(time_table_record_count):
        time_table_record = TimeTableRecord(
            teacher=teacher,
            time_table=time_table,
            subject=subject,
            day_of_week=day_of_week,
            period=period,
        )
        time_table_records.append(time_table_record)
    TimeTableRecord.objects.bulk_create(time_table_records)
    return TimeTableRecord.objects.all()


class TestTimeTables(TestCase):

    def test_create_time_table(self):
        time_table = create_time_table()
        self.assertNotEqual(time_table, None)

    def test_create_time_table_record(self):
        time_table_record = create_time_table_record()
        self.assertNotEqual(time_table_record, None)

    def test_create_time_tables(self):
        create_time_tables(2)
        time_tables = TimeTable.objects.all()
        self.assertEqual(time_tables.count(), 2)

    def test_create_time_table_records(self):
        time_table_records = create_time_table_records(5)
        self.assertEqual(time_table_records.count(), 5)
