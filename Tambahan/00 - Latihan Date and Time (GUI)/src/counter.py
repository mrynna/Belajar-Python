import datetime as dt

def hari(year, month, date):
    tgl = dt.date(year, month, date)
    if dt.date.weekday(tgl) == 0:
        hari = 'Senin'
    elif dt.date.weekday(tgl) == 1:
        hari = 'Selasa'
    elif dt.date.weekday(tgl) == 2:
        hari = 'Rabu'
    elif dt.date.weekday(tgl) == 3:
        hari = 'Kamis'
    elif dt.date.weekday(tgl) == 4:
        hari = "Jum'at"
    elif dt.date.weekday(tgl) == 5:
        hari = 'Sabtu'
    else:
        hari = 'Minggu'
    return hari
    
def tgl(year, month, date):
    tgl = dt.date(year, month, date)
    hari_ini = dt.date.today()
    umur = ((hari_ini - tgl) // 365).days
    bulan_sisa = (((hari_ini-tgl).days)%365) // 30
    umurmu = f"{umur} tahun {bulan_sisa} bulan"
    return umurmu