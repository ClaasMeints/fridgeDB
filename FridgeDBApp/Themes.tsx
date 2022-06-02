import { DefaultTheme } from 'react-native-paper';

declare global {
    namespace ReactNativePaper {
        interface ThemeColors {
            primary: string;
            accent: string;
            background: string;
            surface: string;
            error: string;
            onPrimary: string;
            onAccent: string;
            onBackground: string;
            onSurface: string;
            onError: string;
            disabled: string;
            placeholder: string;
            backdrop: string;
            notification: string;
        }
        interface ThemeBreakpoints {
            small: number;
            medium: number;
            large: number;
        }
        interface Theme {
            roundness: number;
            colors: ThemeColors;
            fonts: ThemeFonts;
            breakpoints: ThemeBreakpoints;
            spacing: number[];
            useTextInputShadows: boolean;
        }
    }
};

const theme = {
    ...DefaultTheme,
    colors: {
        ...DefaultTheme.colors,
        primary: '#24F287',
        accent: '#6A8BA2',
        background: '#F5F7F4',
        onAccent: '#1F1622',
        backdrop: '#1F1622',
        // #B13D56
    },
    roundness: 10,
};

export default theme;