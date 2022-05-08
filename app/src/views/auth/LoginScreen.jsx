import CuToast from "@components/CuToast";
import { BUTTON_MARGIN } from "@constants";
import { useAuth } from "@contexts/authContext";
import loginFieldsJSON from "@fields/login.json";
import FormBuilder from "@form-builder/formBuilder";
import { LoginSVG } from "@helpers/svgIcon";
import { yupResolver } from "@hookform/resolvers/yup";
import { BaseLayout } from "@layout/BaseLayout";
import { loginValidationSchema } from "@validations";
import _ from "lodash";
import React, { useState } from "react";
import { FormProvider, useForm } from "react-hook-form";
import { Button, Colors, LoaderScreen } from "react-native-ui-lib";
import globalS from "../../styles";

const LoginScreen = ({ navigation }) => {
    const formOptions = { resolver: yupResolver(loginValidationSchema) };

    const methods = useForm(formOptions);
    const auth = useAuth();

    const [toastProps, setToastProps] = useState({message: "", isError: false})
    const [displayToast, setDisplayToast] = useState(false);

    const onSubmit = async (datas) => {
        const { success, error, message } = await auth.login(datas);
        if (!success && error) {
                setDisplayToast(true);
                setToastProps({message: message, isError: true});
        }
    };

    return (
        <BaseLayout enablePadding={true} enableSAV>
            {displayToast && (
                <CuToast displayToast={displayToast} setDisplayToast={setDisplayToast} toastProps={toastProps} />
            )}

            {!_.isNil(auth.loading) && auth.loading && (
                <LoaderScreen
                    color={Colors.primary}
                    containerStyle={globalS.centerLoader}
                    overlay={true}
                />
            )}

            <FormProvider {...methods}>
                <FormBuilder fieldsList={loginFieldsJSON} />
                <Button
                    onPress={methods.handleSubmit(onSubmit)}
                    label="Se connecter"
                    size={Button.sizes.large}
                    outlineColor={Colors.primary}
                    style={{ marginVertical: BUTTON_MARGIN - 15, marginTop: 0 }}
                    outline
                />

                <Button
                    onPress={() => navigation.navigate("ForgetPassword")}
                    label="Mot de passe oublié"
                    size={Button.sizes.large}
                    outlineColor={Colors.primary}
                    style={{ marginVertical: BUTTON_MARGIN - 15 }}
                    outline
                />
            </FormProvider>

            <LoginSVG />
        </BaseLayout>
    );
};

export default LoginScreen;
