import { MaterialCommunityIcons } from "@expo/vector-icons";
import { createBottomTabNavigator } from "@react-navigation/bottom-tabs";
import LoginScreen from "@views-auth/LoginScreen";
import SignupScreen from "@views-auth/SignupScreen";
import { BlurView } from "expo-blur";
import React from "react";
import { StyleSheet, TouchableOpacity, View } from "react-native";
import { Colors, Text } from "react-native-ui-lib";

import CustomTabBar from "./CustomTabBar";

const AuthTab = () => {
    const Tab = createBottomTabNavigator();

    return (
        <Tab.Navigator
            initialRouteName="Login"
            backBehavior="history"
            tabBar={(props) => <CustomTabBar {...props} />}
            screenOptions={{
                headerShown: false,
                tabBarActiveTintColor: Colors.primary,
                tabBarInactiveTintColor: Colors.background,
            }}
        >
            <Tab.Screen
                name="Login"
                component={LoginScreen}
                options={{
                    tabBarLabel: "Connexion",
                }}
            />
            <Tab.Screen
                name="Signup"
                component={SignupScreen}
                options={{
                    tabBarLabel: "Inscription",
                }}
            />
        </Tab.Navigator>
    );
};

export default AuthTab;
