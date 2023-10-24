class QSSHelper:

    @staticmethod
    def concat(*styles: str) -> str:
        return ' '.join(styles)

    @staticmethod
    def font_weight(weight: int) -> str:

        if not isinstance(weight, int):
            raise TypeError(type(weight))
        
        if not 1 <= weight <= 1000:
            raise ValueError(weight) 
        
        return f"font-weight: {weight}";

    @staticmethod
    def font_size(font_size: int) -> str:

        if not isinstance(font_size, int):
            raise TypeError(type(font_size))
        
        return f"font-size: {font_size}px;"

    @staticmethod
    def border_radius(border_radius: int) -> str:

        if not isinstance(border_radius, int):
            raise TypeError(type(border_radius))

        return f"""
            border-top-left-radius: {border_radius}px;
            border-top-right-radius: {border_radius}px;
            border-bottom-left-radius: {border_radius}px;
            border-bottom-right-radius: {border_radius}px;
                """

    @staticmethod
    def background_color(hex_color: str) -> str:

        if not isinstance(hex_color, str):
            raise TypeError(type(hex_color))

        return f"background-color: {hex_color};"

    @staticmethod
    def color(rgb_color: tuple) -> str:

        if not isinstance(rgb_color, tuple):
            raise TypeError(type(rgb_color))
        
        if len(rgb_color) != 3:
            raise ValueError(rgb_color)

        return f"color: rgb({rgb_color[0]}, {rgb_color[1]}, {rgb_color[2]});"
    
    @staticmethod
    def letter_spacing(spacing: int) -> str:
        
        if not isinstance(spacing, int):
            raise TypeError(type(spacing))

        return f"letter-spacing: {spacing}px;"