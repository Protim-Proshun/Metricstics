"""The views in an MVC architecture."""
from tkinter import Text
from tkinter.ttk import Frame

from tkmacosx import Button
from tktooltip import ToolTip

# pylint: disable=R0901
# Too many ancestors (8/7) (too-many-ancestors)
# pylint: disable=R0902
# Too many ancestors (8/7) (too-many-ancestors)


class View(Frame):
    """View displays the buttons and text output."""

    def __init__(self, parent):
        """Initialize."""
        super().__init__(parent)

        # create widgets

        # Buttons
        self.button_rd = Button(
            self, text="Read Data", borderless=1, command=self.read_data_clicked
        )
        # self.button_rd.place(x=50, y=50)
        self.button_rd.grid(row=1, column=1)
        ToolTip(self.button_rd, msg="Reading Data from file", delay=2.0)

        self.button_gd = Button(
            self, text="Generate Data", borderless=1, command=self.generate_data_clicked
        )
        # self.button_gd.place(x=50, y=100)
        self.button_gd.grid(row=2, column=1)
        ToolTip(self.button_gd, msg="Generating Data on its own", delay=2.0)

        self.button_vmi = Button(
            self,
            text="View Minimum",
            borderless=1,
            command=self.calculate_minimum_clicked,
        )
        # self.button_vmi.place(x=50, y=150)
        self.button_vmi.grid(row=3, column=1)
        ToolTip(
            self.button_vmi, msg="Calculate Minimum from the generated data", delay=2.0
        )

        self.button_cam.grid(row=4, column=1)
        self.button_cam = Button(
            self,
            text="View Maximum",
            borderless=1,
            command=self.view_maximum_clicked,
        )
        self.button_cam.grid(row=4, column=1)
        ToolTip(
            self.button_cam, msg="Calculate Maximum from the generated data", delay=2.0
        )

        # self.button_vmo = Button(self, text="View Mode", borderless=1)

        self.button_cam = Button(
            self,
            text="View Mode",
            borderless=1,
            command=self.view_mode_clicked,
        )
        # self.button_vmo.place(x=50, y=250)

        self.button_cam.grid(row=5, column=1)
        ToolTip(
            self.button_cam, msg="Calculate Mode from the generated data", delay=2.0
        )

        self.button_cm = Button(
            self,
            text="Calculate Median",
            borderless=1,
            command=self.calculate_median_clicked,
        )
        # self.button_cm.place(x=450, y=50)
        self.button_cm.grid(row=1, column=3)
        ToolTip(
            self.button_cm, msg="Calculate Median from the generated data", delay=2.0
        )

        self.button_cam = Button(
            self,
            text="Calculate Arithmatic Mean",
            borderless=1,
            command=self.calculate_arithmetic_mean_clicked,
        )
        # self.button_cam.place(x=450, y=100)
        self.button_cam.grid(row=2, column=3)
        ToolTip(
            self.button_cam,
            msg="Calculate Arithmetic mean from the generated data",
            delay=2.0,
        )

        self.button_cmad = Button(
            self,
            text="Calculate Mean Absolute Deviation",
            borderless=1,
            command=self.calculate_mean_absolute_deviation_clicked,
        )
        # self.button_cmad.place(x=450, y=200)
        self.button_cmad.grid(row=3, column=3)
        ToolTip(
            self.button_cmad,
            msg="Calculate Mean Absolute Deviation from the generated data",
            delay=2.0,
        )

        self.button_csd = Button(
            self,
            text="Calculate Standard Deviation",
            borderless=1,
            command=self.calculate_standard_deviation_clicked,
        )
        # self.button_csd.place(x=450, y=150)
        self.button_csd.grid(row=4, column=3)
        ToolTip(
            self.button_csd,
            msg="Calculate Standard Deviation from the generated data",
            delay=2.0,
        )

        self.button_sr = Button(self, text="Save Results", borderless=1)
        # self.button_sr.place(x=450, y=250)
        self.button_sr.grid(row=5, column=3)
        ToolTip(self.button_csd, msg="Save Results", delay=2.0)

        # Text
        self.output_text = Text(self, width=50, height=10)
        # self.output_text.place(x=150, y=290)
        self.output_text.grid(row=6, column=2)

        # set the controller
        self.controller = None

    def set_controller(self, controller):
        """Set the controller"""
        self.controller = controller

    def generate_data_clicked(self):
        """Command for generate data button."""
        self.controller.generate_random_data(5)
        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", self.controller.data)

    def calculate_median_clicked(self):
        """Command for calculating the median."""
        result = self.controller.calculate_median()
        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", result["Median"])

    def calculate_arithmetic_mean_clicked(self):
        """Command for calculate arithmatic mean button."""
        result = self.controller.calculate_arithmetic_mean()
        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", result["ArithmeticMean"])

    def view_maximum_clicked(self):
        """Command for view maximum button."""
        result = self.controller.calculate_maximum()
        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", result["Maximum"])

    def view_mode_clicked(self):
        """Command for view mode button."""
        result = self.controller.calculate_mode()
        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", result["Mode"])

    def calculate_mean_absolute_deviation_clicked(self):
        """Command for calculate mean absolute deviation button."""
        result = self.controller.calculate_mean_absolute_deviation()
        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", result["MeanAbsoluteDeviation"])

    def calculate_standard_deviation_clicked(self):
        """Command for calculate standard deviation button."""
        result = self.controller.calculate_standard_deviation()
        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", result["StandardDeviation"])

    def calculate_minimum_clicked(self):
        """Command for calculate standard deviation button."""
        result = self.controller.calculate_minimum()
        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", result["Minimum"])

    def read_data_clicked(self):
        """Command for calculate standard deviation button."""
        self.controller.read_data()
        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", "Reading Data is completed")
