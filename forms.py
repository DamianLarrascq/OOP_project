from tkinter import ttk


class EditForm:
    def __init__(self, frame, record_data):
        col = 0
        rw = 0
        for col_name, value in record_data.items():
            # label
            lb = col_name.replace('_', ' ').title() + ':'
            setattr(self, col_name, ttk.Label(frame, text=lb))
            getattr(self, col_name).grid(row=rw, column=col, padx=5, pady=5)

            # entry
            entry = col_name + '_entry'
            setattr(self, entry, ttk.Entry(frame))
            _entry = getattr(self, entry)
            _entry.grid(row=(rw + 1), column=col, padx=5, pady=5)
            _entry.insert(0, value)
            col += 1
            if col == 4:
                rw += 2
                col = 0


class CreateForm:
    def __init__(self, frame, record_data):
        col = 0
        rw = 0
        for col_name, value in record_data.items():
            # label
            lb = col_name.replace('_', ' ').title() + ':'
            setattr(self, col_name, ttk.Label(frame, text=lb))
            getattr(self, col_name).grid(row=rw, column=col, padx=5, pady=5)

            # entry
            entry = col_name + '_entry'
            setattr(self, entry, ttk.Entry(frame))
            _entry = getattr(self, entry)
            _entry.grid(row=(rw + 1), column=col, padx=5, pady=5)
            # _entry.insert(0, value)
            col += 1
            if col == 4:
                rw += 2
                col = 0
