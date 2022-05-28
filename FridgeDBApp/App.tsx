import * as React from 'react';
import { Text, View } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { MaterialIcons, MaterialCommunityIcons } from '@expo/vector-icons';
import { Provider as PaperProvider, ThemeProvider } from 'react-native-paper';

import FridgeContent from './FridgeContent/FridgeContent';
import theme from './Themes';
import { white } from 'react-native-paper/lib/typescript/styles/colors';


function Profile() {
  return (
    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
      <Text>Profile!</Text>
    </View>
  );
}

function Notifications() {
  return (
    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
      <Text>Notifications!</Text>
    </View>
  );
}

const Tab = createBottomTabNavigator();

function MyTabs() {
  return (
    <Tab.Navigator
      initialRouteName="Fridge"
      screenOptions={{
        tabBarActiveTintColor: theme.fridgePrimary,
      }}
    >
      <Tab.Screen
        name="Fridge"
        component={FridgeContent}
        options={{
          tabBarLabel: 'Fridge',
          tabBarIcon: ({ color, size }) => (
            <MaterialIcons name="kitchen" color={color} size={size} />
          ),
        }}
      />
      <Tab.Screen
        name="Notifications"
        component={Notifications}
        options={{
          tabBarLabel: 'Updates',
          tabBarIcon: ({ color, size }) => (
            <MaterialCommunityIcons name="bell" color={color} size={size} />
          ),
        }}
      />
      <Tab.Screen
        name="Profile"
        component={Profile}
        options={{
          tabBarLabel: 'Profile',
          tabBarIcon: ({ color, size }) => (
            <MaterialCommunityIcons name="account" color={color} size={size} />
          ),
        }}
      />
    </Tab.Navigator>
  );
}

export default function App() {
    return (
        <PaperProvider>
            <NavigationContainer>
                <MyTabs />
            </NavigationContainer>
        </PaperProvider>
    );
}