import { DefaultTheme } from 'react-native-paper';

declare global {
    namespace ReactNativePaper {
      interface ThemeColors {
        primary: string;
        accent: string;
      }
    }
}
  
const theme = {
    ...DefaultTheme,
    // light green 
    fridgePrimary: '#00BFA5',
    // light orange
    fridgeAccent: '#FFD54F',
    // dark green
    fridgeSecondary: '#00796B',
    // dark orange
    fridgeTertiary: '#F57C00',
};

export default theme;