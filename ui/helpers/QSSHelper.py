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
        
        return f"font-weight: {weight};"

    @staticmethod
    def border_none() -> str:
        return "border: none;"

    @staticmethod
    def width(width: int) -> str:

        if not isinstance(width, int):
            raise TypeError(type(width))
        
        return f"width: {width}px;"
    
    @staticmethod
    def height(height: int) -> str:

        if not isinstance(height, int):
            raise TypeError(type(height))
        
        return f"height: {height}px;"
    
    @staticmethod
    def font_size(font_size: int) -> str:

        if not isinstance(font_size, int):
            raise TypeError(type(font_size))
        
        return f"font-size: {font_size}px;"
    
    @staticmethod
    def font_family(font_family: str) -> str:

        if not isinstance(font_family, str):
            raise TypeError(type(font_family))

        return f"font-family: {font_family};"
    
    @staticmethod
    def border_radius(border_radius: int) -> str:

        if not isinstance(border_radius, int):
            raise TypeError(type(border_radius))

        return f"border-radius: {border_radius}px;"

    @staticmethod
    def background_color(hex_color: str) -> str:

        if not isinstance(hex_color, str):
            raise TypeError(type(hex_color))

        return f"background-color: #{hex_color};"

    @staticmethod
    def color(hex_color: str) -> str:

        if not isinstance(hex_color, str):
            raise TypeError(type(hex_color))

        return f"color: #{hex_color};"
    
    @staticmethod
    def letter_spacing(spacing: int) -> str:
        
        if not isinstance(spacing, int):
            raise TypeError(type(spacing))

        return f"letter-spacing: {spacing}px;"