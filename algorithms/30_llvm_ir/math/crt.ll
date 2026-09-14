; ModuleID = 'algorithms/02_c/math/crt.c'
source_filename = "algorithms/02_c/math/crt.c"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-i128:128-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

@.str = private unnamed_addr constant [35 x i8] c"[C CRT] FAILED: x = %lld, want 23\0A\00", align 1
@.str.1 = private unnamed_addr constant [55 x i8] c"[C CRT] x = 23 solves x%%3=2, x%%5=3, x%%7=2 verified\0A\00", align 1

; Function Attrs: nofree nosync nounwind sspstrong memory(argmem: read) uwtable
define dso_local range(i64 -9223372036854775807, -9223372036854775808) i64 @crt(ptr noundef readonly captures(none) %0, ptr noundef readonly captures(none) %1, i32 noundef %2) local_unnamed_addr #0 {
  %4 = alloca i64, align 8
  %5 = alloca i64, align 8
  %6 = icmp sgt i32 %2, 0
  br i1 %6, label %7, label %70

7:                                                ; preds = %3
  %8 = zext nneg i32 %2 to i64
  %9 = and i64 %8, 7
  %10 = icmp ult i32 %2, 8
  br i1 %10, label %15, label %11

11:                                               ; preds = %7
  %12 = and i64 %8, 2147483640
  br label %32

13:                                               ; preds = %32
  %14 = icmp eq i64 %9, 0
  br i1 %14, label %29, label %15

15:                                               ; preds = %13, %7
  %16 = phi i64 [ 0, %7 ], [ %67, %13 ]
  %17 = phi i64 [ 1, %7 ], [ %66, %13 ]
  %18 = icmp ne i64 %9, 0
  tail call void @llvm.assume(i1 %18)
  br label %19

19:                                               ; preds = %19, %15
  %20 = phi i64 [ %16, %15 ], [ %26, %19 ]
  %21 = phi i64 [ %17, %15 ], [ %25, %19 ]
  %22 = phi i64 [ 0, %15 ], [ %27, %19 ]
  %23 = getelementptr inbounds nuw i64, ptr %1, i64 %20
  %24 = load i64, ptr %23, align 8, !tbaa !9
  %25 = mul nsw i64 %24, %21
  %26 = add nuw nsw i64 %20, 1
  %27 = add i64 %22, 1
  %28 = icmp eq i64 %27, %9
  br i1 %28, label %29, label %19, !llvm.loop !11

29:                                               ; preds = %19, %13
  %30 = phi i64 [ %66, %13 ], [ %25, %19 ]
  %31 = zext nneg i32 %2 to i64
  br label %75

32:                                               ; preds = %32, %11
  %33 = phi i64 [ 0, %11 ], [ %67, %32 ]
  %34 = phi i64 [ 1, %11 ], [ %66, %32 ]
  %35 = phi i64 [ 0, %11 ], [ %68, %32 ]
  %36 = getelementptr inbounds nuw i64, ptr %1, i64 %33
  %37 = load i64, ptr %36, align 8, !tbaa !9
  %38 = mul nsw i64 %37, %34
  %39 = getelementptr inbounds nuw i64, ptr %1, i64 %33
  %40 = getelementptr inbounds nuw i8, ptr %39, i64 8
  %41 = load i64, ptr %40, align 8, !tbaa !9
  %42 = mul nsw i64 %41, %38
  %43 = getelementptr inbounds nuw i64, ptr %1, i64 %33
  %44 = getelementptr inbounds nuw i8, ptr %43, i64 16
  %45 = load i64, ptr %44, align 8, !tbaa !9
  %46 = mul nsw i64 %45, %42
  %47 = getelementptr inbounds nuw i64, ptr %1, i64 %33
  %48 = getelementptr inbounds nuw i8, ptr %47, i64 24
  %49 = load i64, ptr %48, align 8, !tbaa !9
  %50 = mul nsw i64 %49, %46
  %51 = getelementptr inbounds nuw i64, ptr %1, i64 %33
  %52 = getelementptr inbounds nuw i8, ptr %51, i64 32
  %53 = load i64, ptr %52, align 8, !tbaa !9
  %54 = mul nsw i64 %53, %50
  %55 = getelementptr inbounds nuw i64, ptr %1, i64 %33
  %56 = getelementptr inbounds nuw i8, ptr %55, i64 40
  %57 = load i64, ptr %56, align 8, !tbaa !9
  %58 = mul nsw i64 %57, %54
  %59 = getelementptr inbounds nuw i64, ptr %1, i64 %33
  %60 = getelementptr inbounds nuw i8, ptr %59, i64 48
  %61 = load i64, ptr %60, align 8, !tbaa !9
  %62 = mul nsw i64 %61, %58
  %63 = getelementptr inbounds nuw i64, ptr %1, i64 %33
  %64 = getelementptr inbounds nuw i8, ptr %63, i64 56
  %65 = load i64, ptr %64, align 8, !tbaa !9
  %66 = mul nsw i64 %65, %62
  %67 = add nuw nsw i64 %33, 8
  %68 = add i64 %35, 8
  %69 = icmp eq i64 %68, %12
  br i1 %69, label %13, label %32, !llvm.loop !13

70:                                               ; preds = %75, %3
  %71 = phi i64 [ 1, %3 ], [ %30, %75 ]
  %72 = phi i64 [ 0, %3 ], [ %92, %75 ]
  %73 = add nsw i64 %72, %71
  %74 = srem i64 %73, %71
  ret i64 %74

75:                                               ; preds = %29, %75
  %76 = phi i64 [ 0, %29 ], [ %93, %75 ]
  %77 = phi i64 [ 0, %29 ], [ %92, %75 ]
  %78 = getelementptr inbounds nuw i64, ptr %1, i64 %76
  %79 = load i64, ptr %78, align 8, !tbaa !9
  %80 = sdiv i64 %30, %79
  call void @llvm.lifetime.start.p0(ptr nonnull %4) #6
  call void @llvm.lifetime.start.p0(ptr nonnull %5) #6
  %81 = call fastcc i64 @egcd(i64 noundef %80, i64 noundef %79, ptr noundef %4, ptr noundef %5)
  %82 = load i64, ptr %4, align 8, !tbaa !9
  %83 = srem i64 %82, %79
  %84 = icmp slt i64 %83, 0
  %85 = select i1 %84, i64 %79, i64 0
  %86 = add nsw i64 %85, %83
  call void @llvm.lifetime.end.p0(ptr nonnull %5) #6
  call void @llvm.lifetime.end.p0(ptr nonnull %4) #6
  %87 = getelementptr inbounds nuw i64, ptr %0, i64 %76
  %88 = load i64, ptr %87, align 8, !tbaa !9
  %89 = mul nsw i64 %88, %80
  %90 = mul nsw i64 %89, %86
  %91 = add nsw i64 %90, %77
  %92 = srem i64 %91, %30
  %93 = add nuw nsw i64 %76, 1
  %94 = icmp eq i64 %93, %31
  br i1 %94, label %70, label %75, !llvm.loop !15
}

; Function Attrs: mustprogress nocallback nofree nosync nounwind willreturn memory(argmem: readwrite)
declare void @llvm.lifetime.start.p0(ptr captures(none)) #1

; Function Attrs: mustprogress nocallback nofree nosync nounwind willreturn memory(argmem: readwrite)
declare void @llvm.lifetime.end.p0(ptr captures(none)) #1

; Function Attrs: nofree nounwind sspstrong uwtable
define dso_local range(i32 0, 2) i32 @main() local_unnamed_addr #2 {
  %1 = alloca i64, align 8
  %2 = alloca i64, align 8
  call void @llvm.lifetime.start.p0(ptr nonnull %1) #6
  call void @llvm.lifetime.start.p0(ptr nonnull %2) #6
  %3 = call fastcc i64 @egcd(i64 noundef 35, i64 noundef 3, ptr noundef %1, ptr noundef %2)
  %4 = load i64, ptr %1, align 8, !tbaa !9
  %5 = srem i64 %4, 3
  %6 = icmp slt i64 %5, 0
  %7 = select i1 %6, i64 3, i64 0
  %8 = add nsw i64 %7, %5
  call void @llvm.lifetime.end.p0(ptr nonnull %2) #6
  call void @llvm.lifetime.end.p0(ptr nonnull %1) #6
  %9 = trunc nsw i64 %8 to i16
  %10 = mul nsw i16 %9, 70
  %11 = srem i16 %10, 105
  call void @llvm.lifetime.start.p0(ptr nonnull %1) #6
  call void @llvm.lifetime.start.p0(ptr nonnull %2) #6
  %12 = call fastcc i64 @egcd(i64 noundef 21, i64 noundef 5, ptr noundef %1, ptr noundef %2)
  %13 = load i64, ptr %1, align 8, !tbaa !9
  %14 = srem i64 %13, 5
  %15 = icmp slt i64 %14, 0
  %16 = select i1 %15, i64 5, i64 0
  %17 = add nsw i64 %16, %14
  call void @llvm.lifetime.end.p0(ptr nonnull %2) #6
  call void @llvm.lifetime.end.p0(ptr nonnull %1) #6
  %18 = trunc nsw i64 %17 to i16
  %19 = mul nsw i16 %18, 63
  %20 = add nsw i16 %19, %11
  %21 = srem i16 %20, 105
  call void @llvm.lifetime.start.p0(ptr nonnull %1) #6
  call void @llvm.lifetime.start.p0(ptr nonnull %2) #6
  %22 = call fastcc i64 @egcd(i64 noundef 15, i64 noundef 7, ptr noundef %1, ptr noundef %2)
  %23 = load i64, ptr %1, align 8, !tbaa !9
  %24 = srem i64 %23, 7
  %25 = icmp slt i64 %24, 0
  %26 = select i1 %25, i64 7, i64 0
  %27 = add nsw i64 %26, %24
  call void @llvm.lifetime.end.p0(ptr nonnull %2) #6
  call void @llvm.lifetime.end.p0(ptr nonnull %1) #6
  %28 = trunc nsw i64 %27 to i16
  %29 = mul nsw i16 %28, 30
  %30 = add nsw i16 %29, %21
  %31 = freeze i16 %30
  %32 = srem i16 %31, 105
  %33 = add nsw i16 %32, 105
  %34 = sext i16 %33 to i64
  %35 = add nsw i64 %34, -105
  %36 = icmp slt i16 %32, 0
  %37 = select i1 %36, i64 %34, i64 %35
  %38 = icmp eq i64 %37, 23
  br i1 %38, label %41, label %39

39:                                               ; preds = %0
  %40 = tail call i32 (ptr, ...) @printf(ptr noundef nonnull dereferenceable(1) @.str, i64 noundef %37)
  br label %43

41:                                               ; preds = %0
  %42 = tail call i32 (ptr, ...) @printf(ptr noundef nonnull dereferenceable(1) @.str.1)
  br label %43

43:                                               ; preds = %41, %39
  %44 = phi i32 [ 1, %39 ], [ 0, %41 ]
  ret i32 %44
}

; Function Attrs: nofree nounwind
declare noundef i32 @printf(ptr noundef readonly captures(none), ...) local_unnamed_addr #3

; Function Attrs: nofree nosync nounwind sspstrong memory(argmem: write) uwtable
define internal fastcc i64 @egcd(i64 noundef %0, i64 noundef %1, ptr noundef nonnull writeonly captures(none) initializes((0, 8)) %2, ptr noundef nonnull writeonly captures(none) initializes((0, 8)) %3) unnamed_addr #4 {
  %5 = alloca i64, align 8
  %6 = alloca i64, align 8
  %7 = icmp eq i64 %1, 0
  br i1 %7, label %16, label %8

8:                                                ; preds = %4
  call void @llvm.lifetime.start.p0(ptr nonnull %5) #6
  call void @llvm.lifetime.start.p0(ptr nonnull %6) #6
  %9 = srem i64 %0, %1
  %10 = call fastcc i64 @egcd(i64 noundef %1, i64 noundef %9, ptr noundef %5, ptr noundef %6)
  %11 = load i64, ptr %6, align 8, !tbaa !9
  %12 = load i64, ptr %5, align 8, !tbaa !9
  %13 = sdiv i64 %0, %1
  %14 = mul nsw i64 %13, %11
  %15 = sub nsw i64 %12, %14
  call void @llvm.lifetime.end.p0(ptr nonnull %6) #6
  call void @llvm.lifetime.end.p0(ptr nonnull %5) #6
  br label %16

16:                                               ; preds = %4, %8
  %17 = phi i64 [ %11, %8 ], [ 1, %4 ]
  %18 = phi i64 [ %15, %8 ], [ 0, %4 ]
  %19 = phi i64 [ %10, %8 ], [ %0, %4 ]
  store i64 %17, ptr %2, align 8, !tbaa !9
  store i64 %18, ptr %3, align 8, !tbaa !9
  ret i64 %19
}

; Function Attrs: nocallback nofree nosync nounwind willreturn memory(inaccessiblemem: write)
declare void @llvm.assume(i1 noundef) #5

attributes #0 = { nofree nosync nounwind sspstrong memory(argmem: read) uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #1 = { mustprogress nocallback nofree nosync nounwind willreturn memory(argmem: readwrite) }
attributes #2 = { nofree nounwind sspstrong uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #3 = { nofree nounwind "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #4 = { nofree nosync nounwind sspstrong memory(argmem: write) uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #5 = { nocallback nofree nosync nounwind willreturn memory(inaccessiblemem: write) }
attributes #6 = { nounwind }

!llvm.module.flags = !{!0, !1, !2, !3}
!llvm.ident = !{!4}
!llvm.errno.tbaa = !{!5}

!0 = !{i32 1, !"wchar_size", i32 4}
!1 = !{i32 8, !"PIC Level", i32 2}
!2 = !{i32 7, !"PIE Level", i32 2}
!3 = !{i32 7, !"uwtable", i32 2}
!4 = !{!"clang version 22.1.8"}
!5 = !{!6, !6, i64 0}
!6 = !{!"int", !7, i64 0}
!7 = !{!"omnipotent char", !8, i64 0}
!8 = !{!"Simple C/C++ TBAA"}
!9 = !{!10, !10, i64 0}
!10 = !{!"long long", !7, i64 0}
!11 = distinct !{!11, !12}
!12 = !{!"llvm.loop.unroll.disable"}
!13 = distinct !{!13, !14}
!14 = !{!"llvm.loop.mustprogress"}
!15 = distinct !{!15, !14}
