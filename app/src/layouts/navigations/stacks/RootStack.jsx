import { routes, screens } from "@layout-navigations/routes";
import AppTab from "@layout-navigations/tabs/AppTab";
import Constants from 'expo-constants';
import {
    createDrawerNavigator,
    DrawerContentScrollView,
    DrawerItem,
} from "@react-navigation/drawer";
import { useAuth } from "@contexts/authContext";
import React from "react";
import { Colors, Text, View, Avatar, Button } from "react-native-ui-lib";
import { StyleSheet } from "react-native";
import { MaterialCommunityIcons } from "@expo/vector-icons";
import Spacer from "@components/Spacer";
import { LayoutView } from "@layout/BaseLayout";
import CuBottomSheet from '@components/CuBottomSheet';
import UserDrawer from "@components/UserDrawer";

const CustomDrawerContent = (props) => {
    // const currentRouteName = props.nav()?.getCurrentRoute().name; // get focused route name
    const auth = useAuth();

    const logout = async () => {
        await auth.logout();
    };

    return (
        <>
            <DrawerContentScrollView {...props}>
                
                <View marginL-10 marginB-25>
                    <UserDrawer />
                </View>

                {routes
                    .filter((route) => route.showInDrawer)
                    .map((route) => {
                        return (
                            <DrawerItem
                                key={route.name}
                                icon={({ color, size }) => {
                                    return route.icon(color, size);
                                }}
                                label={() => (
                                    <Text h6 style={[{ color: Colors.primary }]}>
                                        {route.title}
                                    </Text>
                                )}
                                onPress={() =>
                                    props.navigation.navigate("DrawerStack", {
                                        screen: route.name,
                                    })
                                }
                            />
                        );
                    })}

                <LayoutView>
                    <Spacer />
                </LayoutView>

                <DrawerItem
                    icon={({ color, size }) => (
                        <MaterialCommunityIcons name="share-variant" size={size} color={color} />
                    )}
                    label={() => (
                        <Text h6 style={[{ color: Colors.primary }]}>
                            Partager
                        </Text>
                    )}
                />
                <DrawerItem
                    label={() => (
                        <Text h6 style={[{ color: Colors.primary }]}>
                            Version: {Constants.manifest.version}
                        </Text>
                    )}
                />
            </DrawerContentScrollView>

            <DrawerItem
                style={styles.logoutContainer}
                icon={({ color, size }) => (
                    <MaterialCommunityIcons name="logout" size={size} color={color} />
                )}
                label={() => (
                    <Text h6 style={[{ color: Colors.primary }]}>
                        Se deconnecter
                    </Text>
                )}
                onPress={logout}
            />
        </>
    );
};

const styles = StyleSheet.create({
    logoutContainer: {
        marginBottom: 40,
    },
});

const RootStack = ({ nav }) => {
    const Drawer = createDrawerNavigator();

    const drawerOptions = {
        headerShown: false,
        drawerActiveTintColor: Colors.primary,
        drawerInactiveTintColor: Colors.secondary,
    };

    return (
        <Drawer.Navigator
            initialRouteName="AppTab"
            screenOptions={drawerOptions}
            drawerContent={(props) => <CustomDrawerContent {...props} nav={nav} />}
        >
            <Drawer.Screen name="AppTab" component={AppTab} />
        </Drawer.Navigator>
    );
};

export default RootStack;
